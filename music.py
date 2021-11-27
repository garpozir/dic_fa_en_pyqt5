#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com

import sys
from os.path import expanduser
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):

	def __init__(self):
		super().__init__()
	
		self.currentPlaylist = QMediaPlaylist()
		self.player = QMediaPlayer()
		self.userAction = -1
		self.player.mediaStatusChanged.connect(self.qmp_mediaStatusChanged)
		self.player.stateChanged.connect(self.qmp_stateChanged)
		self.player.positionChanged.connect(self.qmp_positionChanged)
		self.player.volumeChanged.connect(self.qmp_volumeChanged)
		self.player.setVolume(60)
		self.statusBar().showMessage('چیزی وجود ندارد :: %d'%self.player.volume())
		self.homeScreen()
		
	def homeScreen(self):
		self.setWindowTitle('پخش کننده موسیقی')
		self.createMenubar()
		self.createToolbar()
		
		controlBar = self.addControls()
		
		centralWidget = QWidget()
		centralWidget.setLayout(controlBar)
		self.setCentralWidget(centralWidget)
		
		self.resize(200,100)

		self.show()
		
	def createMenubar(self):
		menubar = self.menuBar()
		filemenu = menubar.addMenu('منوی فایل')
		filemenu.addAction(self.fileOpen())
		filemenu.addAction(self.songInfo())
		filemenu.addAction(self.folderOpen())
		filemenu.addAction(self.exitAction())
		
	def createToolbar(self):
		pass
	
	def addControls(self):
		controlArea = QVBoxLayout()	
		seekSliderLayout = QHBoxLayout()
		controls = QHBoxLayout()
		playlistCtrlLayout = QHBoxLayout()
		

		playBtn = QPushButton('پخش')	
		pauseBtn = QPushButton('توقف')	
		stopBtn = QPushButton('بستن')	
		volumeDescBtn = QPushButton('صدا (-)')
		volumeIncBtn = QPushButton('صدا (+)')	
		
		prevBtn = QPushButton('قبلی')
		nextBtn = QPushButton('بعدی')
		
		seekSlider = QSlider()
		seekSlider.setMinimum(0)
		seekSlider.setMaximum(100)
		seekSlider.setOrientation(Qt.Horizontal)
		seekSlider.setTracking(False)
		seekSlider.sliderMoved.connect(self.seekPosition)
		
		seekSliderLabel1 = QLabel('0.00')
		seekSliderLabel2 = QLabel('0.00')
		seekSliderLayout.addWidget(seekSliderLabel1)
		seekSliderLayout.addWidget(seekSlider)
		seekSliderLayout.addWidget(seekSliderLabel2)
		
		playBtn.clicked.connect(self.playHandler)
		pauseBtn.clicked.connect(self.pauseHandler)
		stopBtn.clicked.connect(self.stopHandler)
		volumeDescBtn.clicked.connect(self.decreaseVolume)
		volumeIncBtn.clicked.connect(self.increaseVolume)
		
		controls.addWidget(volumeDescBtn)
		controls.addWidget(playBtn)
		controls.addWidget(pauseBtn)
		controls.addWidget(stopBtn)
		controls.addWidget(volumeIncBtn)
		
		prevBtn.clicked.connect(self.prevItemPlaylist)
		nextBtn.clicked.connect(self.nextItemPlaylist)
		playlistCtrlLayout.addWidget(prevBtn)
		playlistCtrlLayout.addWidget(nextBtn)
		
		controlArea.addLayout(seekSliderLayout)
		controlArea.addLayout(controls)
		controlArea.addLayout(playlistCtrlLayout)
		return controlArea
	
	def playHandler(self):
		self.userAction = 1
		self.statusBar().showMessage('میزان صدا %d'%self.player.volume())
		if self.player.state() == QMediaPlayer.StoppedState :
			if self.player.mediaStatus() == QMediaPlayer.NoMedia:
	
				print(self.currentPlaylist.mediaCount())
				if self.currentPlaylist.mediaCount() == 0:
					self.openFile()
				if self.currentPlaylist.mediaCount() != 0:
					self.player.setPlaylist(self.currentPlaylist)
			elif self.player.mediaStatus() == QMediaPlayer.LoadedMedia:
				self.player.play()
			elif self.player.mediaStatus() == QMediaPlayer.BufferedMedia:
				self.player.play()
		elif self.player.state() == QMediaPlayer.PlayingState:
			pass
		elif self.player.state() == QMediaPlayer.PausedState:
			self.player.play()
			
	def pauseHandler(self):
		self.userAction = 2
		self.statusBar().showMessage('توقف %s موقعیت %s صدا %d'%\
			(self.player.metaData(QMediaMetaData.Title),\
				self.centralWidget().layout().itemAt(0).layout().itemAt(0).widget().text(),\
					self.player.volume()))
		self.player.pause()
			
	def stopHandler(self):
		self.userAction = 0
		self.statusBar().showMessage('میزان صدا %d'%(self.player.volume()))
		if self.player.state() == QMediaPlayer.PlayingState:
			self.stopState = True
			self.player.stop()
		elif self.player.state() == QMediaPlayer.PausedState:
			self.player.stop()
		elif self.player.state() == QMediaPlayer.StoppedState:
			pass
		
	def qmp_mediaStatusChanged(self):
		if self.player.mediaStatus() == QMediaPlayer.LoadedMedia and self.userAction == 1:
			durationT = self.player.duration()
			self.centralWidget().layout().itemAt(0).layout().itemAt(1).widget().setRange(0,durationT)
			self.centralWidget().layout().itemAt(0).layout().itemAt(2).widget().setText('%d:%02d'%(int(durationT/60000),int((durationT/1000)%60)))
			self.player.play()
			
	def qmp_stateChanged(self):
		if self.player.state() == QMediaPlayer.StoppedState:
			self.player.stop()
			
	def qmp_positionChanged(self, position,senderType=False):
		sliderLayout = self.centralWidget().layout().itemAt(0).layout()
		if senderType == False:
			sliderLayout.itemAt(1).widget().setValue(position)
		#update the text label
		sliderLayout.itemAt(0).widget().setText('%d:%02d'%(int(position/60000),int((position/1000)%60)))
	
	def seekPosition(self, position):
		sender = self.sender()
		if isinstance(sender,QSlider):
			if self.player.isSeekable():
				self.player.setPosition(position)
				
	def qmp_volumeChanged(self):
		msg = self.statusBar().currentMessage()
		msg = msg[:-2] + str(self.player.volume())
		self.statusBar().showMessage(msg)
		
	def increaseVolume(self):
		vol = self.player.volume()
		vol = min(vol+5,100)
		self.player.setVolume(vol)
		
	def decreaseVolume(self):
		vol = self.player.volume()
		vol = max(vol-5,0)
		self.player.setVolume(vol)
	
	def fileOpen(self):
		fileAc = QAction('انتخاب موسیقی',self)
		fileAc.setShortcut('Ctrl+O')
		fileAc.setStatusTip('انتخاب موسیقی')
		fileAc.triggered.connect(self.openFile)
		return fileAc
		
	def openFile(self):
		fileChoosen = QFileDialog.getOpenFileUrl(self,'انتخاب فایل موسیقی', expanduser('~'),'Audio (*.mp3 *.ogg *.wav)','*.mp3 *.ogg *.wav')
		if fileChoosen != None:
			self.currentPlaylist.addMedia(QMediaContent(fileChoosen[0]))
	
	def folderOpen(self):
		folderAc = QAction('انتخاب پوشه',self)
		folderAc.setShortcut('Ctrl+D')
		folderAc.setStatusTip('انتخاب پوشه (تمام فایلهای موسیقی داخل پوشه پخش خواهد شد) ')
		folderAc.triggered.connect(self.addFiles)
		return folderAc
	
	def addFiles(self):
		folderChoosen = QFileDialog.getExistingDirectory(self,'انتخاب پوشه موسیقی', expanduser('~'))
		if folderChoosen != None:
			it = QDirIterator(folderChoosen)
			it.next()
			while it.hasNext():
				if it.fileInfo().isDir() == False and it.filePath() != '.':
					fInfo = it.fileInfo()
					print(it.filePath(),fInfo.suffix())
					if fInfo.suffix() in ('mp3','ogg','wav'):
						print('فایل اضافه شد ',fInfo.fileName())
						self.currentPlaylist.addMedia(QMediaContent(QUrl.fromLocalFile(it.filePath())))
				it.next()
			
	def songInfo(self):
		infoAc = QAction('مشخصات فایل',self)
		infoAc.setShortcut('Ctrl+I')
		infoAc.setStatusTip('نمایش مشخصات فایل موسیقی')
		infoAc.triggered.connect(self.displaySongInfo)
		return infoAc
	
	def displaySongInfo(self):
		metaDataKeyList = self.player.availableMetaData()
		fullText = '<table class="tftable" border="0">'
		for key in metaDataKeyList:
			value = self.player.metaData(key)
			fullText = fullText + '<tr><td>' + key + '</td><td>' + str(value) + '</td></tr>'
		fullText = fullText + '</table>'
		infoBox = QMessageBox(self)
		infoBox.setWindowTitle('مشخصات فایل ')
		infoBox.setTextFormat(Qt.RichText)
		infoBox.setText(fullText)
		infoBox.addButton('باشه',QMessageBox.AcceptRole)
		infoBox.show()
	
	def prevItemPlaylist(self):
		self.player.playlist().previous()
	
	def nextItemPlaylist(self):
		self.player.playlist().next()
	
	def exitAction(self):
		exitAc = QAction('&بستن',self)
		exitAc.setShortcut('Ctrl+Q')
		exitAc.setStatusTip('خروج از برنامه')
		exitAc.triggered.connect(self.closeEvent)
		return exitAc
	
	def closeEvent(self,event):
		reply = QMessageBox.question(self,'Message','برای خروج yes را بزنید',QMessageBox.Yes|QMessageBox.No,QMessageBox.Yes)
		
		if reply == QMessageBox.Yes :
			qApp.quit()
		else :
			try:
				event.ignore()
			except AttributeError:
				pass
			
	
if __name__ == '__main__':
	app = QApplication(sys.argv)
	ex = MainWindow()
	sys.exit(app.exec_())

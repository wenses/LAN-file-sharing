import flask, os
from flask import render_template as rt 
from flask import *



app=Flask(__name__)

@app.route('/',methods=['GET','POST'])

def index():


	return rt('index.html')

@app.route('/gotovdfiles',methods=['GET','POST'])
def gotovdfiles():
	global files
	files=os.listdir('files')

	return rt('vdfiles.html',files=files)


@app.route('/gotoupload',methods=['GET','POST'])
def gotoupload():

	return rt('upload.html')


@app.route('/uploader',methods=['GET','POST'])

def uploader():

	if request.method=="POST":
		f=request.files["file"]
		
		os.chdir("files")
		f.save(f.filename)
		os.chdir("..")
			

		return "file uploaded"


@app.route('/view',methods=['GET','POST'])

def view():
	nid=int(request.form['fid'])
	nid=nid-1

	print(files[nid])
	print(os.getcwd())

	return send_file(f'files/{files[nid]}',as_attachment=True)

#app.run(debug=True)
app.run(host="0.0.0.0")

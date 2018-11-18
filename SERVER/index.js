const express = require('express')
var bodyParser = require('body-parser');
var multer  = require('multer');
//var upload = multer(); 
var path = require('path');
var fs = require('fs');



const app = express();

//configure middleware
app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.send('Hello World!')
});

/*const upload = multer({
  dest: "/passport_pictures"
  // you might also want to set some limits: https://github.com/expressjs/multer#limits
});*/
var upload = multer(
    { 
        limits: {
            fieldNameSize: 999999999,
            fieldSize: 999999999
        },
        dest: 'uploads/' }
    );


app.post('/upload', upload.any(), (req, res) => {
	console.log("hello")
	console.log(req.files[0]);

	var tmpPath = req.files[0].path;

	var target_path = 'uploads/' + req.files[0].originalname;

	//Save file
	var src= fs.createReadStream(tmpPath);
	var dest = fs.createWriteStream(target_path);
	console.log('print')

	src.pipe(dest);
  src.on('end', () => { 
    	res.send({a:"ok"}); });
  src.on('error', (err) => { console.log(err); res.send({error: "upload failed"}); });

	
	//Send the response from the checks
	//res.setHeader('Content-Type', 'application/json');
	//res.send({success:true , a:'OK'});
});

app.listen(8000, () => {
  console.log('Example app listening on port 8000!')
});
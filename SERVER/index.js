const express = require('express')
var bodyParser = require('body-parser');


const app = express();

//configure middleware
app.use(bodyParser.json());

app.get('/', (req, res) => {
  res.send('Hello World!')
});

app.post('/verifyImage', upload.any(), (req, res) => {
	console.log(req.files);
	 res.setHeader('Content-Type', 'application/json');
	res.send(json.stringify({a:'OK'}));
})

app.listen(8000, () => {
  console.log('Example app listening on port 8000!')
});
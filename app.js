const express = require('express')
const cors = require('cors')
const app = express()


var PythonShell = require('python-shell');


var fs = require('fs')

var bodyParser = require('body-parser')

app.use( bodyParser.json() );       // to support JSON-encoded bodies
app.use(bodyParser.urlencoded({     // to support URL-encoded bodies
  extended: true
})); 


app.use(cors());

/*
let runPy = new Promise(function(sucess, nosuccess) {

    const { spawn } = require('child_process');
    const pyprog = spawn('python',['./RunModel.py']);

    pyprog.stdout.on('data', function(data) {

        sucess(data);

    });
    pyprog.stderr.on('data', (data) => {

        nosuccess(data);

    });

});*/

app.post('/', (req, res) => {

    var comment = req.body.comnt;
    console.log(comment);
    /*fs.writeFile('commentinput.txt',comment,function(err){
        if (err) {
            console.log(err)
        }
        else
        {
            console.log('written');
        }
    })*/



        var options = {
          mode: 'text',
          args: [comment]
        };
         
        PythonShell.run('RunModel.py', options, function (err, results) {
          if (err) throw err;
          // results is an array consisting of messages collected during execution 
          console.log('results: %j', results);
          res.send(results[0])
        });



   /* runPy.then(function(fromRunpy) {
        console.log(fromRunpy.toString());
        res.end(fromRunpy);
    });*/

})
app.listen(4000, () => console.log('app listening on port 4000!'))


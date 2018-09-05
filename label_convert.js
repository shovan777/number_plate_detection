/**
 * convert the bbox label to json format
 * @type {Object}
 */
const fs = require('fs');




// var fs = require('fs');

if (process.argv.length <= 2) {
  console.log("Usage: " + __filename + " path/to/directory");
  process.exit(-1);
}

var path = process.argv[2];
// const out_dir = 'new_data';

function readFiles(dirname, onFileContent, onError) {
  fs.readdir(dirname, function(err, filenames) {
    if (err) {
      onError(err);
      return;
    }
    filenames.forEach(function(filename) {
      fs.readFile(dirname + filename, 'utf-8', function(err, content) {
        if (err) {
          onError(err);
          return;
        }
        onFileContent(dirname, filename, content);
      });
    });
  });
}

readFiles(path, (dirname, filename, content) => {

  // create the json model of annotation
  var model = {
    tags: ["test"],
    objects: [],
    size: {
      height: 512,
      width: 512
    }
  }

  // extract data from the content
  var lines = content.split("\n");
  // console.log(lines);
  lines.forEach((line) => {
    if(line) {
      var coord = line.split(" ");
      // console.log(coord);

      // add each box as a separate object
      model.objects.push({
        classTitle: "plate_bbox",
        points: {
          exterior:[
            [parseFloat(coord[1]), parseFloat(coord[2])],
            [parseFloat(coord[3]), parseFloat(coord[4])]
          ],
          interior: []
        }
      });
    }

  });
  // console.log(JSON.stringify(model));

  // write the annotation model in json file
  // console.log(dirname + filename.split('.')[0] + '.json');
  fs.writeFileSync(
    dirname + filename.split('.')[0] + '.json',
    JSON.stringify(model),
    'utf8',
    (err) => {
      if(err) throw err;
      // console.log("file write done");
    }
  );
});

const cows = require(`cowsay`);
module.exports.speak = str => cows.say({"text" : str});

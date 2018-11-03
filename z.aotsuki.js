const Discord = require(`discord.js`);
client = new Discord.Client();

client.on(`ready`, () => {
    console.log(`${client.user.tag} is now online!`);
    client.user.setActivity("つーなーいだ");
});

client.on(`message`, (message) => {
    if(message.author.bot ||
message.channel.type === `dm`) return;

    if(message.content === `碧月`){
        message.channel.send(`なんでしょう？何なりとお申し付けを`);
    }
    //^muu ○○
    if(message.author.bot) return;
    var args = message.content.trim().split(/ +/g);
    var command = args.shift();
    if(command === '?aa'){
        if(args[0]){
            message.channel.send(args[0]);
        }else{
            message.channel.send('やり方が違います！');
        }
        message.delete();
    }
    if(message.author.bot) return;
    var args = message.content.trim().split(/ +/g);
    var command = args.shift();
    if(command === '?a'){
        if(args[0]){
            message.channel.send(args[0]);
        }else{
            message.channel.send('やり方が違います！');
        }
   }
   if (message.content.match(/文月/)) {
        
    message.delete(100)
　　}
if (message.content.match(/h!hentai/)) {
        
    message.delete(100)
　　}
});


client.login(`NDgzMDkxMzAxNDU0MzE1NTY5.DmOaIg.jo6FOUfkEwIrNlOjPlWpJ2-BSmQ`);
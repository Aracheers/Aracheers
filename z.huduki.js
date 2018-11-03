const Discord = require(`discord.js`);
client = new Discord.Client();

client.on(`ready`, () => {
    console.log(`${client.user.tag} is now online!`);
    client.user.setActivity("(ﾟ∀ﾟ)ｱﾋｬ");
});

client.on(`message`, (message) => {
    if(message.author.bot ||
message.channel.type === `dm`) return;

    if(message.content === `Hello`){
        message.channel.send(`Hello!`);
    }
    //^muu ○○
    if(message.author.bot) return;
    var args = message.content.trim().split(/ +/g);
    var command = args.shift();
    if(command === '!aa'){
        if(args[0]){
            message.channel.send(args[0]);
        }else{
            message.channel.send('間違ってるぞくそったれ');
        }
        message.delete();
    }
    if(message.author.bot) return;
    var args = message.content.trim().split(/ +/g);
    var command = args.shift();
    if(command === '!a'){
        if(args[0]){
            message.channel.send(args[0]);
        }else{
            message.channel.send('間違ってるぞくそったれ');
        }
   }


});


client.login(`NDgzMDc3MDIzNjk5NDM1NTIw.DmOMOA.zL4ArnO1tNdJFY8b6zaVVi5mgwA`);
const fs=require('node:fs')
const express=require('express');
const { send } = require('node:process');
const {spawn} = require('child_process')

const app=express();
const port=9000;

app.use(express.static('./'));

app.get('/', (req, res) => {res.redirect("/home")});

app.get(['/home'], (req, res) =>{
    res.writeHead(200, "success", { "content-type": 'text/html' });
    res.write(fs.readFileSync(`./${req.url}.html`));
    res.end();
})

app.get('/test', (req, res)=>{
    const python = spawn('python', ['python/main.py']) //Incompleto

    result=[]
    result[0]='test'
    res.send(result)
    res.end()
})

app.listen(port, () =>
    {
        console.log(
            `Server is running on %shttp://localhost:${port}%s`,
            '\x1b[38;5;2m','\x1b[0m');
    });
const fs=require('node:fs')
const express=require('express');
const { send } = require('node:process');
const {spawn} = require('child_process')

const app=express();
const port=9000;

app.use(express.static('./'));

app.get('/', (req, res) => {res.redirect("/home")});

app.get(['/home','/map'], (req, res) =>{
    res.writeHead(200, "success", { "content-type": 'text/html' });
    res.write(fs.readFileSync(`./${req.url}.html`));
    res.end();
})

app.get(['/graph','/mapdata'], (req, res)=>{
    console.log(req.url)
    var result
    const cidade = req.query.cidade
    const estado = "SP"
    const time_range_start = parseInt(req.query.range_start)
    const time_range_end = parseInt(req.query.range_end)
    console.log(`${cidade}\n${time_range_start}\n${time_range_end}`)

    script=(req.url.includes('/mapdata')) ? 'python/map.py' : 'python/main.py'
    const pychild = spawn('/bin/python3', [script, cidade, estado, time_range_start, time_range_end],{
        serialization:'json'
    })

    pychild.stdout.on('data', (data) =>{
        var str = JSON.parse(data.toString())
        console.log(str)
        result=str
    })

    pychild.on('exit', ()=>{
        res.send(result)
        res.end()
    })

    pychild.stderr.on('data', (data)=>{
        console.error(`stderr: ${data}`)
    })
})

app.listen(port, () =>
    {
        console.log(
            `Server is running on %shttp://localhost:${port}%s`,
            '\x1b[38;5;2m','\x1b[0m');
    });
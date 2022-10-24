self.addEventListener('message', e => {
    console.log("Worker IN")
    getSentiments(e.data.id,e.data.ind)
    
})
const getSentiments = async(id,ind)=>{
    try{
        const res  = await fetch(`http://127.0.0.1:8000/youtubeassist/sentiment/${id}`)
        const data = await res.json()
        self.postMessage({"data": data,"ind":ind})
    }
    catch(err){
        console.log(err)
        self.postMessage({"data": {"Negative":0,"Positive":0,"Neutral":0},"ind":ind})
    }
    self.close()
}
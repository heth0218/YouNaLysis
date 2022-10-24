const {fetchSubreddit} = require('fetch-subreddit');
 
function isReddit(x){
    if(x.toString().indexOf("https://www.reddit.com/") != -1 && x.toString().indexOf("gallery") == -1){
        return x;
    }
}
function isNotNull(e){
    return e!=null
}
function pretty(obj) {
   const x = obj[0].urls.map(isReddit)
   const xl = x.filter(isNotNull)
  return JSON.stringify(xl[0]);
}
const entityList = async (ents) => {
    let finalList = []
    for(let e of ents){
        try{
            const resp = await fetchSubreddit(e.split(' ').join(''))
            if(resp){
                let x = pretty(resp); 
                finalList.push(x);
            }
        }catch(err){
            console.log("1",err)
        }
    }
    return finalList
}

module.exports=entityList
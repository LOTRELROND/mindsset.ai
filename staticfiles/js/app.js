console.log("hi")
var UpdateFav = document.getElementsByClassName('update-fav')


for(var i =0; i<UpdateFav.length; i++){
    UpdateFav[i].addEventListener('click',function(){
        var postId = this.dataset.post
        var action = this.dataset.action
        console.log('postId:',postId, 'action:',action)

        console.log(user)
        if(user === 'AnonymousUser'){
            console.log('user not logged in')
        }
        else{
            updateFav(postId,action)
            if(action=="add"){
                alert("post added into favorites")
            }
            else{
                alert("post deleted from favorites")
            }
        }
    })
}


function updateFav(postId,action){
    
    var url = '/updateFav/'

    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        },
        body:JSON.stringify({
            'postId':postId,
            'action':action
        })

    })

        .then((response) => {
            return response.json()
        })

        .then((data) =>{
            console.log('data:',data)
            location.reload()
        })

        
}

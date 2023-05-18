//NavBar
function hideIconBar(){
    var iconBar = document.getElementById("iconBar");
    var navigation = document.getElementById("navigation");
    iconBar.setAttribute("style", "display:none;");
    navigation.classList.remove("hide");
}

function showIconBar(){
    var iconBar = document.getElementById("iconBar");
    var navigation = document.getElementById("navigation");
    iconBar.setAttribute("style", "display:block;");
    navigation.classList.add("hide");
}

//Comment
function showComment(){
    var commentArea = document.getElementById("comment-area");
    commentArea.classList.toggle("hide");
    let comment = document.getElementById('btnComment')
    if (commentArea.classList.contains('hide')){
        comment.textContent = 'Commenter'
    }else{
        comment.textContent = 'Ne pas commenter'
    }
}

//Reply
function showReplies(id){
    let replyArea = document.getElementById(id);
    replyArea.classList.toggle('hide');
    let reply = document.getElementById('btnReply')
    if (replyArea.classList.contains('hide')){
        reply.textContent = 'Repondre'
    }else{
        reply.textContent = 'Ne pas repondre'
    }
}

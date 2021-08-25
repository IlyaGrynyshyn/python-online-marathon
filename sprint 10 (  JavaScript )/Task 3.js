function longestLogin(loginList) {
    return loginList.reduce(function (longerword,curentword) {
        if (curentword.length >= longerword.length)
            return curentword;
        else
            return longerword
    })
}


console.log(longestLogin(["user1", "user2", "333", "user4", "aa"]))
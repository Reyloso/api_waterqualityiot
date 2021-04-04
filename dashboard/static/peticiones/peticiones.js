


async function get(url) {
    return await axios.get(url).then(result => {
        if(result.code ==! 1){
            console.log(result.message)
        }else{
            return result.data
        }
    }).catch((err) => {console.log(err.response)})
}

//post data
async function post(url, data, csrf_token){
    return  await axios.post(url, data, {headers: {"X-CSRFToken": csrf_token,'Content-Type': 'application/json'}}).then(result => {
        if(result.data.code == 2){
            // Toast.fire({
            //     icon: 'warning',
            //     title: String(result.data.message)
            // })
            return result
        }else if(result.data.code ==! 1){
            // Toast.fire({
            //     icon: 'warning',
            //     title: "Ha ocurrido un error contacte con el administrador"
            // })
            return result
        }else{
            // Toast.fire({
            //     icon: 'success',
            //     title:  String(result.data.message)
            // })
            // title: "Regitro Exitoso!"
            return result.data
        }
    }).catch((err) => {
        console.log(err)
        // Toast.fire({
        //     icon: 'error',
        //     title: String(err)
        // })
        
    })
}

//put data
async function put(url, data, csrf_token){
    return  await axios.put(url, data, {headers: {"X-CSRFToken": csrf_token,'Content-Type': 'application/json' }}).then(result => {
        if(result.data.code == 2){
            // Toast.fire({
            //     icon: 'warning',
            //     title: String(result.data.message)
            // })
        }else if(result.data.code ==! 1){
            // Toast.fire({
            //     icon: 'warning',
            //     title: "Ha ocurrido un error contacte con el administrador"
            // })
        }else{
            // Toast.fire({
            //     icon: 'success',
            //     title:  String(result.data.message)
            // })
            // title: "Regitro Exitoso!"
            return result.data
        }
    }).catch((err) => {
        // Toast.fire({
        //     icon: 'error',
        //     title: String(err)
        // })
    })
}

async function deleted(url, csrf_token){
    return  await axios.delete(url, {headers: {"X-CSRFToken": csrf_token,'Content-Type': 'application/json' }}).then(result => {
        if(result.data.code == 2){
            // Toast.fire({
            //     icon: 'warning',
            //     title: String(result.data.message)
            // })
        }else if(result.data.code ==! 1){
            // Toast.fire({
            //     icon: 'warning',
            //     title: "Ha ocurrido un error contacte con el administrador"
            // })
        }else{
            // Toast.fire({
            //     icon: 'success',
            //     title:  String(result.data.message)
            // })
            // title: "Regitro Exitoso!"
            return result.data
        }
    }).catch((err) => {
        // Toast.fire({
        //     icon: 'error',
        //     title: String(err)
        // })
    })
}

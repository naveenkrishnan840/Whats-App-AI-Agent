
export const RequestService = (path, data) => {
    const header_data = {
        'Content-Type': 'application/json'
    }
    if (localStorage.getItem("token")){
        header_data["Authorization"] = `Bearer ${localStorage.getItem("token")}`
    }
    var body = JSON.stringify(data) 
    var path = `http://3.111.243.223:8085/${path}`
    return fetch(path, {
        method: "POST",
        headers: header_data,
        body: body
    }).then(res => res.json());
}


export const RequestUrlService = (path, data) => {
    const header_data = {
        'Content-Type': 'application/json'
    }
    if (localStorage.getItem("token")){
        header_data["Authorization"] = `Bearer ${localStorage.getItem("token")}`
    }
    var body = JSON.stringify(data) 
    var path = `http://65.1.139.145:8085${path}`
    return fetch(path, {
        method: "POST",
        headers: header_data,
        body: body
    }).then(res => res.json())
}


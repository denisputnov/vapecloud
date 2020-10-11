class Bot {
    constructor(token) {
        this.base_url = `https://api.telegram.org/bot${token}`
        this._request = new XMLHttpRequest()
    }
    /**
     * 
     * @param {object} params - params for message {chat_id, text}
     */
    sendMessage(params) {
        this._request.open('POST', `${this.base_url}/sendMessage?chat_id=${params.chat_id}&text=${params.text}&parce_mode=html`)
        this._request.send()
    }
}

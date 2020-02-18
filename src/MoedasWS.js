import React from 'react'

class MoedasWS extends React.Component {

    ws = new WebSocket('ws://localhost:8765/moedas')
    constructor(props) {
        super(props)
        this.state = {
            moedas:[]
        }
    }

    componentDidMount() {
        this.ws.onopen = () => {
            console.log('conectado')
        }
    }

    render() {
        return (
            <div>
                WS       
            </div>
        )    
    }
}

export default MoedasWS;

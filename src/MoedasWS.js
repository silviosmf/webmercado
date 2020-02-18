import React from 'react'

class MoedasWS extends React.Component {


    ws = new WebSocket('ws://localhost:8765/')

    listaMoedas = [];

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
        this.ws.onmessage = evt => {
            const message = JSON.parse(evt.data)
            let valores = []
            valores = message;
            
            this.setState({          
                // moedas: this.listaMoedas.reverse()
                moedas:valores
            })
            this.listaMoedas.push(valores[0]);
            console.log(this.listaMoedas)
            // console.log(this.state.moedas)
        }

        this.ws.onclose = () => {
            console.log('descontectado')
        }
    }

    
    render() {
        return (            
            <div>
                <ul>
                    {this.listaMoedas.map(item => {return <li>{item['sigla']} - {item['cotacao']}</li>})}   
                </ul>                
        </div>
    )
    }
}

export default MoedasWS;

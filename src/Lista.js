import React from 'react';

class Lista extends React.Component {

  render () {
    const lista = ['item 1', 'item 2']
    return (
      <div>
          <ul>
              {lista.map(item => (
                  <li>
                      Sigla:{item}
                  </li>
              ))}
          </ul>
      </div>
    );
  }

}

export default Lista;
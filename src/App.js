import React from 'react';

import MoedasGraficoDiarioPercentual from './MoedasGraficoDiarioPercentual';

function App() {
  return (    
      <div class="row">
        <div class="col-sm-3">
            <div className="App">
              <MoedasGraficoDiarioPercentual/>
            </div>
        </div>
        <div class="col-sm-3">
            <div className="App">
              <MoedasGraficoDiarioPercentual/>
            </div>
        </div>
        <div class="col-sm-3">
            <div className="App">
              <MoedasGraficoDiarioPercentual/>
            </div>
        </div>
      </div>
    
  );
}

export default App;

import ChatBotBody from './components/chatBotBody';
import LoginPage from './components/login';
import {createContext, useContext, useState} from "react";
import {BrowserRouter as Router, Routes,Route} from "react-router-dom";

export const stateContext = createContext();

function App() {
  const [userDet, setUserDet] = useState([]);

  return (
    <stateContext.Provider value={{userDet, setUserDet}}>
      <Router>
        <Routes>
          <Route path='/login' element={<LoginPage/>}/>
          <Route path='/whatappAI' element={<ChatBotBody/>}/>
        </Routes>
      </Router>
    </stateContext.Provider>
  );
}

export default App;

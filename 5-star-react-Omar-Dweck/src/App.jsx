import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Heroname from './Components/herobanner-name'
import ToDoList from './ToDoList'
// import Footer from './Components/Footer'

function App() {
  const [count, setCount] = useState(0)
  const value = "Welcome to 5$tar"




  return (



    <>
    <Heroname  data={value} />

  
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
       
       
      </div>

      <div>
        <ToDoList/>
      </div>
      

     


    </>
  )
}

export default App

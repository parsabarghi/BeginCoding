import { useState } from "react"
import { useNavigate } from "react-router-dom"
import api from '../api'
import { ACCESS_TOKEN, REFRESH_TOKEN } from "../constants";

const Form = ({route, method}) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("")
  const navigate = useNavigate()

  const head_text = method === 'login' ? "Hey My Friend!" : "Welcome"
  const name = method === 'login' ? 'Login' : "Register"

  const handleSubmit = async (e) => {
    e.preventDefault();

    try{
      const res = await api.post(route, { username, password })
      if (method === "login") {
        localStorage.setItem(ACCESS_TOKEN, res.data.access);
        localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
        navigate('/')
      }else {
        navigate("/login")
      }
    }catch (err) {
      alert(err)
    }finally {

    }
  }


    return (
        <div className="bg-[#1A2238] h-screen w-screen">
        <div className="flex flex-col items-center flex-1 h-full justify-center px-4 sm:px-0">
          <div className="flex rounded-lg shadow-lg w-full sm:w-3/4 lg:w-1/2 bg-white sm:mx-0" style={{ height: '500px' }}>
            <div className="flex flex-col w-full md:w-1/2 p-4">
              <div className="flex flex-col flex-1 justify-center mb-8">
                <h1 className="text-4xl text-center font-thin">{head_text}</h1>
                <div className="w-full mt-4">
                  <form className="form-horizontal w-3/4 mx-auto" onSubmit={handleSubmit}>
                    <div className="flex flex-col mt-4">
                      <input
                        id="email"
                        type="text"
                        className="flex-grow h-8 px-2 border rounded border-grey-400"
                        name="email"
                        value={username}
                        required
                        placeholder="Your Full Name"
                        onChange={(e) => setUsername(e.target.value)}
                      />
                    </div>
                    <div className="flex flex-col mt-4">
                      <input
                        id="password"
                        type="password"
                        className="flex-grow h-8 px-2 rounded border border-grey-400"
                        name="password"
                        value={password}
                        required
                        placeholder="Password"
                        onChange={(e) => setPassword(e.target.value)}
                      />
                    </div>
                    <div className="flex flex-col mt-8">
                      <button
                        type="submit"
                        className="bg-[#1A2238] hover:bg-blue-700 text-white text-sm font-semibold py-2 px-4 rounded"
                      >
                        {name}
                      </button>
                    </div>
                  </form>
                </div>
              </div>
            </div>
            <div
              className="hidden md:block md:w-1/2 rounded-r-lg"
              style={{
                background: "url('https://images.unsplash.com/photo-1515965885361-f1e0095517ea?ixlib=rb-1.2.1&auto=format&fit=crop&w=3300&q=80')",
                backgroundSize: 'cover',
                backgroundPosition: 'center center',
              }}
            ></div>
          </div>
        </div>
      </div>
    )
}
export default Form
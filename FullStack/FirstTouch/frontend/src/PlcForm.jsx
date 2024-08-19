import { useState } from "react";

const PlcFrom = () => { 
    const [name, setName] = useState("");
    const [ip, setIp] = useState("");

    const onSubmit = async (e) => {
        e.preventDefault()
        const data = {
            name, 
            ip 
        }
        const url = "http://127.0.0.1:5000/create_plc"
        const option = {
            method: "POST", 
            headers: {
                "Content-Type": "application/json"
            }, 
            body: JSON.stringify(data)    
        }
        const response = await fetch(url, option)
        if (response.status !== 201 && response.status !== 200) {
            const data = await response.json()
            alert(data.message)
        } else {
            // successful
        }
    }
    

    return (
    <form onSubmit={onSubmit}>
        <div>
            <label htmlFor="name">
                <input 
                type="text"
                id = "name"
                value={name}
                onChange={(e) => setName(e.target.value)} 
                />
            </label>
        </div>
        <div>
            <label htmlFor="ip">
                <input 
                type="text"
                id = "ip"
                value={ip}
                onChange={(e) => setIp(e.target.value)} 
                />
            </label>
        </div>
        <button type="submit">Create PLC</button>
    </form>
    )
}

export default PlcFrom
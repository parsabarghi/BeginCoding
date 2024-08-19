import React from "react";

const PlcList = ({ PLCs }) => {
    return (
    <div>
        <h2>PLC LIST</h2>
        <table>
                <thead>
                    <tr>
                        <th>IP</th>
                        <th>Name</th>
                        <th>Actions</th>

                    </tr>
                </thead>
            <tbody>
                {PLCs.map((plc) => (
                    <tr key={plc.id}>
                        <td>{plc.ip}</td>
                        <td>{plc.Name}</td>
                        <td>
                            <button>Update</button>
                            <button>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
    );
};
export default PlcList;
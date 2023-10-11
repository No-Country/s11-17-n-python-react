import React from 'react'

const index = ({ list, onChange }) => {

    return (
        <div className="select-form">
            <label for="exampleInputPassword1" className="form-label">Selecciona tu país</label>
            <select className="mb-3 form-select" aria-label="Default select example" onChange={onChange}>
                {list?.map((country, index) => <option value={index}> {country} </option>)}
            </select>
        </div>
    )
}

export default index
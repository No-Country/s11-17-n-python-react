import React from "react";

const MenuRabbitPerfil = () =>{
    return <>
    <div>
        <h6> Datos del conejo: </h6>
        <table className="table">
  <thead>
    <tr>
      <th scope="col" className="table-secondary">Estado</th>
      <th scope="col">Vivo</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th scope="row" className="table-light">Peso</th>
      <td>8 kg</td>
    </tr>
    <tr>
      <th scope="row" className="table-secondary">Raza</th>
      <td>California</td>
    </tr>
    <tr>
      <th scope="row" className="table-light">Edad</th>
      <td>8 meses</td>
    </tr>
    <tr>
      <th scope="row" className="table-secondary">Color</th>
      <td>Blanco</td>
    </tr>
    <tr>
      <th scope="row" className="table-light">Genotipo</th>
      <td>-</td>
    </tr>
    <tr>
      <th scope="row" className="table-secondary">Crias vivas</th>
      <td>4</td>
    </tr>
    <tr>
      <th scope="row" className="table-light">Total de Crias</th>
      <td>14</td>
    </tr>
  </tbody>
</table>
    </div>
    </>
  );
};

MenuRabbitPerfil.propTypes = {
  rabbitData: PropTypes.object.isRequired,
};

export default MenuRabbitPerfil;
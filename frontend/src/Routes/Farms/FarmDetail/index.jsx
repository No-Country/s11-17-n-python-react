import { useEffect } from 'react';
import { useLoaderData, useNavigate } from 'react-router-dom';
import { useHttp } from '../../../hooks/useHttp';
import useHttpGetWithPagination from "../../../hooks/useHttpGetWithPagination";
import { apiUrls } from "../../../utils/links";
import styles from './styles.module.css';


const FarmDetail = () => {
  const navigate = useNavigate();
  const farmId = useLoaderData();
  const { isLoading, data, error, sendRequest } = useHttp();
  const { isLoading: isLoadingCages, data: dataCages, error: errorCages, sendRequest: sendRequestCages } = useHttpGetWithPagination()
  
    
    useEffect(() => {
      sendRequestCages(`${apiUrls.urlCages}?${farmId}`)
      sendRequest(`${apiUrls.urlFarms}${farmId}`);
    }, [sendRequest, farmId, sendRequestCages]);
  return (
    <div>
      {data && (
      <div className='d-flex flex-column'>
        <h2 className='mt-5 d-flex justify-content-center align-items-center '>
          Detalles de la granja {farmId}
        </h2>

        <img
            src={data.photo}
            alt='farmProfile'
            width={'350'}
            className='img-fluid rounded mx-auto d-block mt-4 '
          />
          
        <div className='d-flex flex-column justify-content-center align-items-center'>
          <p className='mb-4 fst-italic'>{data.address}</p>
        </div>

        <h4 className='my-3 title d-flex flex-column justify-content-center align-items-center'>{data.name}</h4>
        <p className='text-break lh-sm text-center'>{data.description}</p>
        <section>

          {dataCages && (
            <div className='d-flex flex-column justify-content-center align-items-center'>
              <h4 className='mt-5'>Jaulas de {data.name}</h4>
              <div className='d-flex flex-wrap justify-content-center align-items-center'>
                {dataCages.map((cage) => (
                  <div
                    key={cage.id}
                    className={`card d-inline-flex flex-column border border-2 border-success-subtle rounded mx-5 mt-4 shadow bg-body-tertiary rounded align-self-center ${styles.maxSize}`}
                    //redirect to cage detail page when clicking on card
                    onClick={() => navigate(`/farms/${farmId}/cages/${cage.id}`)}
                  >
                    <img
                      src={cage.photo}
                      alt='cageProfile'
                      className={`card-img-top img-fluid ${styles.imageSize}`}
                    />
                    <div className='card-body'>
                      <h5 className='card-title'>Jaula Numero {
                        dataCages.indexOf(cage) + 1
                      }</h5>
                      <p className='card-text'>Numero de conejos en la jaula: <span className='fw-medium'>{cage.count_rabbits}</span></p>
                      <p className='card-text'>Precio de la Jaula: <span className='fw-medium'>${cage.price} MXN</span></p>
                      <p className='card-text'>Peso total: <span className='fw-medium'>{cage.total_weight} Kg</span></p>
                      <span>{cage.id}</span>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}
        </section>
      </div>
      )}

      {isLoading && (
        <h2 className='text-muted text-center m-5 p-5'>Cargando...</h2>
      )}

      {error && (
        <h2 className='text-danger text-center m-5 p-5'>
          Ha ocurrido un error, intente de nuevo
        </h2>
      )}

      {!isLoading && !error && !data && (
        <h2 className='text-muted text-center m-5 p-5'>
          No hay granjas disponibles
        </h2>
      )}
    </div>
  );
};

export default FarmDetail;
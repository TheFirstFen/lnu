import React, { useState, useEffect } from "react"
import { Card, CardGroup, Row, Col } from 'react-bootstrap';
import './cards.css';

const Cards = (props) => {
  const [chart, setChart] = useState([])
  const baseUrl = "https://termostatuller.billenius.com/sql"

  useEffect(() => {
    const f = async () => {

      await fetch(`${baseUrl}?get_last=true&username=${props.loginCreds.username}&password=${props.loginCreds.password}`,

        { method: "GET" })
        .then(response => response.json())
        .then(json => {
          setChart(json)
        })
    }
    f()
    setInterval(f, 15_000); // Refresh every 30 seconds 
  }, [baseUrl])


  return (
    <CardGroup>
      <Row xs={2} md={2} className="g-5">
        <Col>
          <Card className='Cards' border={"danger"} style={{ width: '15rem' }}>
            <Card.Header>Temperatur</Card.Header>
            <Card.Body as="h1">{`${chart?.celsius} \u2103`}</Card.Body>
            <Card.Footer>Mättes {chart?.created_at}</Card.Footer>
          </Card>
        </Col>
        <Col>
          <Card className='Cards' border={"primary"} style={{ width: '15rem' }}>
            <Card.Header>Luftfuktighet</Card.Header>
            <Card.Body as="h1">{chart?.humidity} %</Card.Body>
            <Card.Footer>Mättes {chart?.created_at}</Card.Footer>
          </Card>
        </Col>
      </Row>
    </CardGroup>
  );
}

export default Cards;

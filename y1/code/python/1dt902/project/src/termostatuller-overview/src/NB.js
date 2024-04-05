import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';

export default function NB(props) {
    return (
        <Navbar sticky="top" collapseOnSelect expand="lg" bg="dark" variant="dark">
            <Container>
                <Navbar.Brand href="#home"><img src="/logo.png" width="30" height="30"></img> Termostatuller</Navbar.Brand>
                <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                <Navbar.Collapse id="responsive-navbar-nav">
                    <Nav className="me-auto">
                        {/* Toggle links on off based on if on loginpage */}
                        {props.signin ?
                            <></> :
                            <>
                                <Nav.Link href="#last">Senaste</Nav.Link>
                                <Nav.Link href="#24h">24 timmar</Nav.Link>
                                <Nav.Link href="#7d">7 dagar</Nav.Link>

                            </>}
                    </Nav>
                    <Nav>
                        <Nav.Link href="mailto:lb224hk@student.lnu.se">Kontakta oss</Nav.Link>
                    </Nav>
                </Navbar.Collapse>
            </Container>
        </Navbar>
    );
}
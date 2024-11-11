import NB from "./NB"
import { TwentyFourHLineChart, SevenDaysLineChart } from './LineChart';
import Cards from './cards.js';

export default function MainPage(props) {
    return <>
        <NB signin={false}/>
        <div className="App">
            <div id={"last"} ></div> {/* Dummy för scoll*/}
            <br />
            <br />
            <h1>Senaste mätning</h1>
            <br />
            <div style={{ display: 'flex', justifyContent: 'center' }}>
                <Cards loginCreds={props.loginCreds} />
            </div>
            <div id={"24h"} ></div> {/* Dummy för scoll*/}
            <br />
            <br />
            <div>
                <h1>Senaste 24 timmarna</h1>
                <br />
                <TwentyFourHLineChart style={{ display: 'flex', justifyContent: 'center' }} loginCreds={props.loginCreds} />
            </div>
            <div id={"7d"} ></div> {/* Dummy för scoll*/}
            <br />
            <br />
            <div>
                <h1>Senaste 7 dagarna</h1>
                <br />
                <SevenDaysLineChart style={{ display: 'flex', justifyContent: 'center' }} loginCreds={props.loginCreds} />
            </div>
        </div >
    </>
}
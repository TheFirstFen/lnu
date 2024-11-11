import React, { useState, useEffect } from "react"
import { Line } from "react-chartjs-2"
import { Chart as ChartJJS, LineElement, CategoryScale, LinearScale, PointElement, Legend, Tooltip, Filler } from "chart.js"


ChartJJS.register(CategoryScale,
    LinearScale,
    LineElement,
    PointElement,
    Legend,
    Tooltip,
    Filler
);

function getSQLDate(minutesBackFromNow) {
    const earlier = Date.now() - (60 * 1000 * minutesBackFromNow);
    return new Date(earlier).toISOString().slice(0, 16);
}

function TwentyFourHLineChart(props) {
    var [chart, setChart] = useState([])
    const baseUrl = "https://termostatuller.billenius.com/sql"

    var count = 1
    useEffect(() => {
        const f = async () => {
            await fetch(`${baseUrl}?since-date=${getSQLDate(60 * 24)}&username=${props.loginCreds.username}&password=${props.loginCreds.password}`,
                { method: "GET" })
                .then(response => response.json())
                .then(json => {
                    console.log(`(${count++}) Refreshing...`)
                    setChart(json)
                })
        }
        f()
        setInterval(f, 15_000); // Refresh every 15 seconds 
    }, [baseUrl])

    var data = {
        datasets: [
            {
                label: "Temperatur (\u2103)",
                data: chart?.map(a => { return { y: a.celsius, x: a.created_at } }),
                borderWidth: 1,
                borderColor: '#AA4A44',
                backgroundColor: '#EC5800',
            },
            {
                label: "Luftfuktighet (%)",
                data: chart?.map(a => { return { y: a.humidity, x: a.created_at } }),
                borderWidth: 1,
                borderColor: '#36A2EB',
                backgroundColor: '#000080',
            }]
    };

    const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { position: "top" },
            title: { display: true, text: `Temperatur ("\u2103")` }
        },
        scales: {
            y: {
                // min: 5,
                // max: 40,
                beginAtZero: false
            }
        },
        legend: {
            labels: {
                fontSize: 14
            }
        }
    }

    return (
        <div>
            <Line data={data} options={options} height={600} />
        </div >
    )
}

function SevenDaysLineChart(props) {
    const [chart, setChart] = useState([])
    const baseUrl = "https://termostatuller.billenius.com/sql"

    useEffect(() => {
        const f = async () => {
            await fetch(`${baseUrl}?since-date=${getSQLDate(24 * 60 * 7)}&username=${props.loginCreds.username}&password=${props.loginCreds.password}`,
                { method: "GET" })
                .then(response => response.json())
                .then(json => {
                    // console.log(json);
                    setChart(json)
                })
        }
        f()
        setInterval(f, 15_000); // Refresh every 15 seconds 
    }, [baseUrl])

    console.log(chart)
    var data = {
        datasets: [
            {
                label: "Temperatur (\u2103)",
                data: chart?.map(a => { return { y: a.celsius, x: a.created_at } }),
                borderWidth: 1,
                borderColor: '#AA4A44',
                backgroundColor: '#EC5800',
            },
            {
                label: "Luftfuktighet (%)",
                data: chart?.map(a => { return { y: a.humidity, x: a.created_at } }),
                borderWidth: 1,
                borderColor: '#36A2EB',
                backgroundColor: '#000080',
            }]
    };

    const options = {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { position: "top" },
            title: { display: true, text: "Temperatur" }
        },
        scales: {
            y: {
                beginAtZero: false
            }
        },
        legend: {
            labels: {
                fontSize: 14
            }
        }
    }

    return (
        <div>
            <Line data={data} options={options} height={600} />
        </div >
    )
}

export { TwentyFourHLineChart, SevenDaysLineChart }

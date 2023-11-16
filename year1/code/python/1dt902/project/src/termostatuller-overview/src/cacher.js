

const baseUrl = "https://termostatuller.billenius.com/sql"
class Cacher {
    constructor() {
        this.lastFetched = new Date()
    }


    getDateMinutesEarlier(minutesBackFromNow) {
        const earlier = Date.now() - (60 * 1000 * minutesBackFromNow);
        return new Date(earlier).toISOString().slice(0, 16);
    }

    getWeek() {

    }
}

export default Cacher;
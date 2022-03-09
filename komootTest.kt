enum class Sport { HIKE, RUN, TOURING_BICYCLE, E_TOURING_BICYCLE }

data class Summary(val sport: Sport, val distance: Int)

fun main() {
    val sportStats = listOf(
        Summary(Sport.HIKE, 92),
        Summary(Sport.RUN, 77),
        Summary(Sport.TOURING_BICYCLE, 322),
        Summary(Sport.E_TOURING_BICYCLE, 656)
    )

    // Write kotlin code to print the top sport by distance excluding eBikes.
    findLongestDistanceTraveledSport(sportStats)
}

fun findLongestDistanceTraveledSport(inputList: List<Summary>) {
    var longestDistance = 0
    var sportIndex = -1

    // creates a sports list excluding eBikes
    val filteredList: List<Summary> = inputList.filter {
        it.sport != Sport.E_TOURING_BICYCLE
    }

    filteredList.forEachIndexed { index, element ->
        if (element.distance >= longestDistance) {
            longestDistance = element.distance
            sportIndex = index
        }
    }
    println("The top sport is: ${inputList[sportIndex].sport} and the distance traveled is: ${longestDistance}m")
}

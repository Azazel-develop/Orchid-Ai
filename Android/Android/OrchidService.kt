package com.orchid.ai


class OrchidService {


    var listening = false


    fun startListening(){

        listening = true

        println(
            "Orchid is listening"
        )

    }


    fun stopListening(){

        listening = false

    }

}

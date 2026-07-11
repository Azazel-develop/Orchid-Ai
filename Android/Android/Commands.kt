package com.orchid.ai


object Commands {


    fun process(command: String): String {


        return when {


            command.contains("hello") ->
                "Hello, I am Orchid."


            command.contains("timer") ->
                "Timer activated."


            command.contains("open") ->
                "Opening application."


            else ->
                "I do not know this command yet."

        }

    }

}

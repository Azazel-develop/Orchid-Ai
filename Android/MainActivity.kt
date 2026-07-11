package com.orchid.ai

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent


class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {

        super.onCreate(savedInstanceState)

        setContent {

            OrchidScreen()

        }
    }
}


fun OrchidScreen() {

    println("Orchid Mobile Started")

}

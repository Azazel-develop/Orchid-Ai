package com.orchid.ai

import android.content.Context
import android.media.AudioRecord
import android.media.MediaRecorder


class Microphone(private val context: Context) {


    fun startListening() {

        println("Orchid microphone active")

        // Real audio capture will connect here
        // AudioRecord API handles microphone input

    }


    fun stopListening() {

        println("Microphone stopped")

    }

}

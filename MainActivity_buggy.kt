package edu.asu.cse535.meseretictactoe

import android.app.NotificationChannel
import android.app.NotificationManager
import android.content.Context
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.enableEdgeToEdge
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.lifecycle.viewmodel.compose.viewModel
import androidx.navigation.compose.rememberNavController

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        enableEdgeToEdge()

        ResultsStore.init(applicationContext)


        showDebugNotificationBuggy()

        setContent {
            AppRoot()
        }
    }

    //Bug added for demonstration
    private fun showDebugNotificationBuggy() {
        val channelId = "demo_channel"
        val channelName = "Demo Channel"


        val channel = NotificationChannel(
            channelId,
            channelName,
            NotificationManager.IMPORTANCE_DEFAULT
        )

        val manager = getSystemService(Context.NOTIFICATION_SERVICE) as NotificationManager
        manager.createNotificationChannel(channel)
    }
}

@Composable
fun AppRoot() {
    val navController = rememberNavController()
    val gameVm: GameViewModel = viewModel()

    Surface(color = MaterialTheme.colorScheme.background) {
        NavRoot(
            nav = navController,
            gameVm = gameVm
        )
    }
}


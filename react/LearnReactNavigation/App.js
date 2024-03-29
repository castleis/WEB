import React from 'react'
import { NavigationContainer } from '@react-navigation/native'
import { createNativeStackNavigator } from '@react-navigation/native-stack'

import Greeting from './components/Greeting'
import HomeScreen from './screens/HomeScreen'
import DetailScreen from './screens/DetailScreen'

const Stack = createNativeStackNavigator()

const App = () => {
    return (
    <NavigationContainer>
        <Stack.Navigator>
            <Stack.Screen 
                name="Home" 
                component={HomeScreen}
                options={{
                    title: '홈',
                }}
            />
            <Stack.Screen name='Detail' component={DetailScreen}/>
        </Stack.Navigator>
    </NavigationContainer>
    )
}

export default App
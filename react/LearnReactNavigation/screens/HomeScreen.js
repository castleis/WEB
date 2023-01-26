import React from 'react'
import {View, Button} from 'react-native'

function HomeScreen({navigation}) {
    return (
        <View>
            <Button 
                title="Detail 1 열기"
                onPress={() => navigation.navigate('Detail', {id: 1})}
                // onPress={() => navigation.push('Detail')} 도 가능
                // {id: 숫자} : 라우트 파라미터 (새로운 화면을 보여줄 때 의존해야 하는 어떤 값이 있으면 라우트 파라미터를 설정)
                //  라우트 파라미터는 객체 타입으로 설정 ex) {username: 'john}
            />
            <Button 
                title="Detail 2 열기"
                onPress={() => navigation.navigate('Detail', {id: 2})}
                // onPress={() => navigation.push('Detail')} 도 가능
            />
            <Button 
                title="Detail 3 열기"
                onPress={() => navigation.navigate('Detail', {id: 3})}
                // onPress={() => navigation.push('Detail')} 도 가능
            />
        </View>
    )
}

export default HomeScreen
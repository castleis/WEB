import { TabRouter } from '@react-navigation/native'
import React from 'react'
import {View, Text, StyleSheet, Button} from 'react-native'

function DetailScreen() {
    return (
        <View style={styles.block}>
            <Text style={styles.text}>id: {route.params.id}</Text>

            <Button 
                title='next'
                onPress={() => navigation.push('Detail', {id: route.params.id + 1})}
                // navigation은 push와 달리 새로 이동할 화면이 현재 화면과 같으면
                // 새로운 화면을 쌓지 않고 파라미터만 변경
                // push는 새로운 화면이 스택에 쌓여가면서 화면이 전환됨
                // 즉 폰에서 뒤로가기를 누르면 이전 Detail 화면이 열림
            />

            {/* 뒤로가기 & 처음으로 가기 */}
            <Button title='뒤로가기' onPress={() => navigation.pop()}/>
            <Button title='처음으로' onPress={() => navigation.popToTop()}/>
        </View>
    )
}

const styles = StyleSheet.create({
    block: {
      flex: 1,
      alignItems: 'center',
      justifyContent: 'center',
    },
    text: {
      fontSize: 48,
    },
    buttons: {
        flexDirection: 'row',
    },
})

export default DetailScreen
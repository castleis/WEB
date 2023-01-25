## 설계
#### App.js
컴포넌트 트리구조의 가장 상단에 있는 App.js에서는 Store를 정의. CounterListContainer와 Store를 연결해줌으로 Store가 관리하는 전역적인 데이터를 공유
#### src/actions
액션과 액션 생성자를 정의!
- 액션의 종류
    - INCREMENT : type과 index를 갖음
    - DECREMENT : type과 index를 갖음
    - ADD : type을 갖음
    - REMOVE : type을 갖음
#### src/components
Presentational 컴포넌트의 DOM 마크업과 스타일을 담당
#### src/containers
Redux와 Presentaional 컴포넌트 연결을 담당
#### src/reducers
action 타입에 따른 데이터의 변화를 순수함수로 정의

## Presentational and Container 패턴
유지보수와 재사용성을 고려한 패턴..?
### Container 컴포넌트
- 데이터를 다루는 부분.
- 동작(behavior) 로직
- Redux와 관련 있음
- 렌더링 되어야 할 데이터를 props로 데이터 처리 능력이 없는 컴포넌트인 Presentational 컴포넌트로 전달
### Presentational 컴포넌트
- DOM 마크업과 스타일 담당
- 데이터 처리 능력 없음
- 부모 컴포넌트로부터 받은 props 데이터와 콜백(callback)을 사용
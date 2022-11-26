import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

import createPersistedState from 'vuex-persistedstate'
import router from '../router'

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],

  state: {
    URL : 'http://localhost:8000',
    token : null,
    username : null,
    moviesList : null,
    user_id : null,
    nickName : null,
    adult : null
    // journal_detail : null,
  },

  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
    moviesList(state) {
      return state.moviesList
    },
    journal_detail(state) {
      return state.journal_detail
    }
  
 

  },

  mutations: {
    SAVE_TOKEN (state, token) {
      state.token = token
    },
    SAVE_USER_INFO (state, data) {
      state.username = data.username
      state.user_id = data.pk
    },
    DELETE_USER_INFO (state) {
      state.username = null
      state.user_id = null
      state.token = null
      state.nickName = null
      state.adult=false
      
    },
    SAVE_MOVIES_LIST (state, data) {
      state.moviesList = data
    },
    SAVE_USER_PROFILE (state, data) {
      state.nickName = data.nickname
      state.adult = data.adult
    }
    // SAVE_JOURNAL_DETAIL (state, journal_detail) {
    //   state.journal_detail = journal_detail
    // },
    // DELETE_JOURNAL_DETAIL (state) {
    //   state.journal_detail = null
    // } 
    
  },
  actions: {
    // 회원가입
    signUp (context, payload) {
      
      // 일단 사인 업!
      axios({
        method: 'post',
        url: context.state.URL + '/accounts/signup/',
        data: payload.forSignUp
      })
        .then((res) => {
          context.commit('SAVE_TOKEN', res.data.key)
          return res.data.key
        })
        .then((token) => {
          axios({
            method: 'post',
            url : context.state.URL + '/profile/create/',
            headers: {
              Authorization: `Token ${token}`
            },
            data: payload.forProfile
          })
          .then(() => {
            context.dispatch('getUserInfo')
          })
        })
        .then(() => {
          router.push({name: 'index'})
        })
        .catch((err) => {
          console.log(err)
          if (err.response.data.non_field_errors[0] === 
            "The two password fields didn't match.") {
              alert('비밀번호 확인을 정확히 입력해주세요')
            } else if (err.response.data.non_field_errors[0] === 
            "The password is too similar to the username.") {
              alert('아이디와 비밀번호가 너무 비슷합니다')          
            } else if (err.response.data.password1.includes("This password is too short. It must contain at least 8 characters.")
             ) {
              alert('비밀번호가 너무 짧습니다, 8자 이상으로 작성하세요')
            } else if (err.response.data.password1.includes("This password is too common."))
            {
              alert('비밀번호가 너무 쉽습니다')
            } else if (err.response.data.username.includes("A user with that username already exists.")) {
              alert("이미 존재하는 아이디 입니다")
            }
            
    })
  },
    // 로그인
    logIn (context, payload) {
      const username = payload.username
      const password = payload.password
      axios({
        method: 'post',
        url: context.state.URL + '/accounts/login/',
        data: {
          username: username,
          password: password
        }})
        .then((res) => {
  
          context.commit('SAVE_TOKEN', res.data.key)
        })
        .then(() => {
          context.dispatch('getUserInfo')
        })
        .then(() => {
          router.push({name: 'index'})
        })
        .catch((err) => {
          console.log(err)
          if (err.response.data.non_field_errors[0] === 
            'Unable to log in with provided credentials.') {
              alert('ID나 비빌번호를 정확히 입력해주세요')
            }
        })
        },

    // 로그아웃
    logOut (context) {
      axios({
        method: 'post',
        url: context.state.URL + '/accounts/logout/',
        })
        .then(() => {

          context.commit('DELETE_USER_INFO')
        })
        .then(() => {
          router.push({name: 'index'})
        })
        .catch((err) => console.log(err))
        },
    
    // 유저 정보 가져오기
    getUserInfo (context) {
      axios({
        method: 'get',
        url: context.state.URL + '/accounts/user/',
        headers: {
          Authorization: `Token ${context.state.token}`
        },
        })
        .then((res) => {
          context.commit('SAVE_USER_INFO', res.data)
        })
        .then(() => {
         context.dispatch('getUserProfile')
        })
        .catch((err) => {
          console.log(err)
  
        })
        },
        getUserProfile(context) {
          axios({
            method: 'get',
            url: context.state.URL + `/profile/${context.state.user_id}/`,
            headers: {
            Authorization: `Token ${context.state.token}`
            },
          })
        .then((res) => {
          context.commit('SAVE_USER_PROFILE', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
      },
        // 비밀번호 변경
        changePassword(context, payload) {
          axios({
            method: 'post',
            url: context.state.URL + '/accounts/password/change/',
            headers: {
              Authorization: `Token ${context.state.token}`
            },
            data: payload
          })
          .then(() => {
            alert('비밀번호가 변경되었습니다! 다시 로그인 해주세요!')
          })
          .then(() => context.dispatch('logOut'))
          .catch((err) => {
            console.log(err)
            if (err.response.data.old_password[0] === 
              'Your old password was entered incorrectly. Please enter it again.') {
                alert('이전 비밀번호가 틀렸습니다.')
              } else if (err.response.data.new_password2[0] === "The password is too similar to the username.") {
                alert('비밀번호가 ID와 너무 유사합니다.')
              } else if (err.response.data.new_password2[0] === "This password is too short. It must contain at least 8 characters.") {
                alert('비밀번호가 너무 짧습니다. 8자 이상으로 작성해주세요')
              } else if (err.response.data.new_password2[0] === "This password is too common.") {
                alert('비밀번호가 너무 쉽습니다.')
              }
            
          })
        },

        updateProfile(context, payload) {
          axios({
            method: 'put',
            url: context.state.URL + `/profile/detail/`,
            headers : {
              Authorization: `Token ${context.state.token}`
            },
            data : payload
          })
          .then(() => {
            context.dispatch('getUserProfile')
          })
          .then(() => {
            router.push({name: 'index'})
          })
          .catch((err) => console.log(err))
        },




    // 영화 전체 가져오기
    getMyMovies(context, user_id) {
        axios({
          method: 'get',
          url: context.state.URL + `/movies/${user_id}/my_movie_list/`,
        })
        .then((res) => {
          context.commit('SAVE_MOVIES_LIST', res.data)
        })
        .catch((err) => console.log(err))
      }
      
  

    


    },


  modules: {
  }
})

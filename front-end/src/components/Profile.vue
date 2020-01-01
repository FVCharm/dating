<template>
  <el-main class="detailMain">
      <el-row>
        <el-col :span="6">
          <div style="margin:12px;">
            <el-card>
              <div style="text-align: center">
                <el-avatar :size="120" :src="require('../assets/icons/3.jpg')"></el-avatar>
              </div>
              <div style="text-align: center; margin: 24px 0;">
                <el-tag effect="plain" style="padding: 0 30px;font-size: 18px;">个人信息</el-tag>
              </div>
              <div style="margin-left: 12px;">
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">婚姻状况：{{livelyForm.status}}</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">是否有小孩：{{livelyForm.children}}</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">住房情况：{{livelyForm.house}}</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">买车情况：{{livelyForm.car}}</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">是否吸烟: {{livelyForm.smoke}}</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">是否喝酒：{{livelyForm.drink}}</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">健康状况：{{livelyForm.health}}</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">宗教信仰：{{livelyForm.religion}}</span>
                </div>
              </div>
            </el-card>
          </div>
        </el-col>
        <el-col :span="12">
          <div style="margin:12px;">
            <el-card :body-style="{ padding: '8px' }">
              <div style="text-align: center; margin: 0 6px;">
                <el-carousel height="260px" indicator-position="outside">
                  <el-carousel-item>
                    <el-image
                      :src="
                        require('../assets/icons/girl1.jpg')
                      "
                    ></el-image>
                  </el-carousel-item>
                  <el-carousel-item>
                    <el-image
                      :src="
                        require('../assets/icons/girl2.jpg')
                      "
                    ></el-image>
                  </el-carousel-item>
                  <el-carousel-item>
                    <el-image
                      :src="
                        require('../assets/icons/girl4.jpg')
                      "
                    ></el-image>
                  </el-carousel-item>
                  <el-carousel-item>
                    <el-image
                      :src="
                        require('../assets/icons/girl5.jpg')
                      "
                    ></el-image>
                  </el-carousel-item>
                  <el-carousel-item>
                    <el-image
                      :src="
                        require('../assets/icons/girl6.jpg')
                      "
                    ></el-image>
                  </el-carousel-item>
                </el-carousel>
              </div>
              <div align="center" style="margin-top: 12px;">
                <el-button icon="el-icon-chat-square" type="primary">发消息</el-button>
                <el-button icon="el-icon-star-off" type="primary">关注</el-button>
                <el-button icon="el-icon-collection" type="primary">联系方式</el-button>
                <el-button icon="el-icon-circle-check" type="primary">已认证信息</el-button>
              </div>
              <el-divider></el-divider>
              <div style="text-align: center; margin: 20px 0;">
                <el-tag effect="plain" style="padding: 0 30px;font-size: 18px;">个人信息</el-tag>
              </div>
              <el-row>
                <el-col :span="12">
                  <div style="margin-left: 24px;">
                    <div style="margin-bottom: 16px;">
                      <span style="color: #8c939d;">用户昵称：{{personalForm.username}}</span>
                    </div>
                    <div style="margin-bottom: 16px;">
                      <span style="color: #8c939d;">工作城市：</span>
                    </div>
                    <div style="margin-bottom: 16px;">
                      <span style="color: #8c939d;">每月收入：{{ personalForm.salary }}</span>
                    </div>
                  </div>
                </el-col>
                <el-col :span="12">
                  <div style="margin-left: 12px;">
                    <div style="margin-bottom: 16px;">
                      <span style="color: #8c939d;">我的学历：{{personalForm.degree}}</span>
                    </div>
                    <div style="margin-bottom: 16px;">
                      <span style="color: #8c939d;">我的身高：{{personalForm.height}}</span>
                    </div>
                    <div style="margin-bottom: 16px;">
                      <span style="color: #8c939d;">我的职业：</span>
                    </div>
                  </div>
                </el-col>
              </el-row>
            </el-card>
          </div>
        </el-col>
        <el-col :span="6">
          <div style="margin:12px;">
            <el-card>
              <div style="text-align: center"></div>
              <div style="text-align: center; margin: 20px 0;">
                <el-tag effect="plain" style="padding: 0 30px;font-size: 18px;">我喜欢的类型</el-tag>
              </div>
              <div style="margin-left: 12px;">
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">年龄：</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">月薪：</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">工作城市：</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">住房情况：</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">买车情况：</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">是否吸烟喝酒</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">健康状况：</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">是否有小孩：</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">学历：</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">身高：</span>
                </div>
                <div style="margin-bottom: 16px;">
                  <span style="color: #8c939d;">是否有照片：</span>
                </div>
              </div>
            </el-card>
          </div>
        </el-col>
      </el-row>
    </el-main>
</template>

<script>
import store from '../store.js'

export default {
  name: 'Profile', // this is the name of the component
  data () {
    return {
      sharedState: store.state,
      user: '',
      livelyForm: {
        status: '',
        children: '',
        religion: '',
        health: '',
        house: '',
        car: '',
        smoke: '',
        drink: ''
      },
      personalForm: {
        username: '',
        workPlace: [],
        salary: '',
        height: '',
        degree: '',
        job: ''
      }
    }
  },
  methods: {
    getUser (id) {
      const path = `/users/${id}`
      this.$axios.get(path)
        .then((response) => {
          this.livelyForm.status = response.data.livelyForm.status
          this.livelyForm.children = response.data.livelyForm.children
          this.livelyForm.religion = response.data.livelyForm.religion
          this.livelyForm.health = response.data.livelyForm.health
          this.livelyForm.house = response.data.livelyForm.house
          this.livelyForm.car = response.data.livelyForm.car
          this.livelyForm.smoke = response.data.livelyForm.smoke
          this.livelyForm.drink = response.data.livelyForm.drink
          this.personalForm.username = response.data.personalForm.username
          this.personalForm.salary = response.data.personalForm.salary
          this.personalForm.height = response.data.personalForm.height
          this.personalForm.degree = response.data.personalForm.degree
          console.log(response.data.livelyForm.status)
        })
        .catch((error) => {
          // eslint-disable-next-line
            console.error(error)
        })
    }
  },
  created () {
    // eslint-disable-next-line camelcase
    const user_id = this.$route.params.id
    console.log(user_id)
    this.getUser(user_id)
  },
  // 当 id 变化后重新加载数据
  beforeRouteUpdate (to, from, next) {
    console.log(to.params.id)
    this.getUser(to.params.id)
    next()
  }
}
</script>

<style scoped>

</style>

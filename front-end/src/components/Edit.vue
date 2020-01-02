<template>
  <el-container>
    <el-main class="editMain">
      <el-row style="margin-top: 48px;">
        <el-tabs :tab-position="'left'">
          <el-tab-pane label="基本信息">
            <section class="personal">
              <el-row>
                <el-col :offset="1" :span="11">
                  <el-card :body-style="{ padding: '36px 10px 24px 12px' }">
                    <div slot="header" style="text-align:center">个人信息</div>
                    <el-col :offset="3" :span="17" style="text-align:center">
                      <el-form :model="personalForm" label-width="100px" ref="personalForm">
                        <el-form-item label="用户昵称">
                          <el-input v-model="personalForm.username"></el-input>
                        </el-form-item>
                        <el-form-item label="工作城市">
                          <div id="app" style="text-align: left;">
                            <el-cascader
                              :options="cityOptions"
                              size="large"
                              v-model="personalForm.workPlace"
                            ></el-cascader>
                          </div>
                        </el-form-item>
                        <el-form-item label="每月收入">
                          <el-select placeholder="选择真实的月收入" v-model="personalForm.salary">
                            <el-option
                              :key="item.value"
                              :label="item.label"
                              :value="item.value"
                              v-for="item in salaryOptions"
                            ></el-option>
                          </el-select>
                        </el-form-item>
                        <el-form-item align="left" label="我的学历">
                          <el-select placeholder="请选择您的真实学历" v-model="personalForm.degree">
                            <el-option
                              :key="item.value"
                              :label="item.label"
                              :value="item.value"
                              v-for="item in degreeOptions"
                            ></el-option>
                          </el-select>
                        </el-form-item>
                        <el-form-item label="真实身高">
                          <el-select placeholder="请选择身高" v-model="personalForm.height">
                            <el-option
                              :key="item"
                              :label="item + 130 + ' cm'"
                              :value="item + 130 + ' cm'"
                              v-for="item in 99"
                            ></el-option>
                          </el-select>
                        </el-form-item>
                        <el-form-item label="我的职业">
                          <el-select placeholder v-model="personalForm.job">
                            <el-option label="1" value="0"></el-option>
                            <el-option label="2" value="1"></el-option>
                            <el-option label="3" value="2"></el-option>
                          </el-select>
                        </el-form-item>
                      </el-form>
                    </el-col>
                    <div style="text-align:center">
                      <el-button :plain="false" @click="savePersonalForm" type="primary">保存修改</el-button>
                    </div>
                  </el-card>
                </el-col>
                <el-col :offset="1" :span="10" style="background-color: white;">
                  <el-row>
                    <el-card :body-style="{ padding:'24px 0 6px' }">
                      <div class="clearfix" slot="header">
                        <span style="margin-left: 156px">重要信息</span>
                        <el-button
                          @click="modifyDialog = true"
                          style="float: right; padding: 3px 0"
                          type="text"
                        >修改</el-button>
                        <el-dialog :visible.sync="modifyDialog" title="提示" width="30%">
                          <span>更改重要信息时，需要进行身份证认证</span>
                          <span class="dialog-footer" slot="footer">
                            <el-button @click="modifyDialog = false">稍后认证</el-button>
                            <el-button @click="modifyDialog = false" type="primary">
                              <router-link tag="div" to="/auth">现在认证</router-link>
                            </el-button>
                          </span>
                        </el-dialog>
                      </div>
                      <el-row style="text-align:center">
                        <el-col :span="12">
                          <div class="text item">实名：xxx</div>
                          <div class="text item">生日：xxx</div>
                        </el-col>
                        <el-col :span="12">
                          <div class="text item">民族：xxx</div>
                          <div class="text item">籍贯：xxx</div>
                        </el-col>
                      </el-row>
                    </el-card>
                  </el-row>
                  <el-row style="margin-top: 20px">
                    <el-card>
                      <div class="clearfix" slot="header" style="text-align:center">
                        <span>联系方式</span>
                      </div>
                      <div style="padding-right:48px; margin-top:18px">
                        <el-form :model="contactForm" label-width="80px" ref="contactForm">
                          <el-form-item label="QQ">
                            <el-input placeholder="输入QQ号码"></el-input>
                          </el-form-item>
                          <el-form-item label="微信">
                            <el-input placeholder="输入微信号"></el-input>
                          </el-form-item>
                          <el-form-item label="手机号">
                            <el-input placeholder="输入手机号"></el-input>
                          </el-form-item>
                        </el-form>
                        <div style="text-align:center">
                          <el-button @click="saveContactForm" type="primary">保存资料</el-button>
                        </div>
                      </div>
                    </el-card>
                  </el-row>
                </el-col>
              </el-row>
            </section>
          </el-tab-pane>
          <el-tab-pane label="生活资料">
            <section>
              <el-row>
                <el-col :offset="1" :span="22">
                  <el-card style="text-align:center">
                    <div slot="header">
                      <span>生活资料</span>
                    </div>
                    <el-form
                      :inline="true"
                      :model="livelyForm"
                      label-width="100px"
                      ref="livelyForm"
                      style="margin-top:20px;"
                    >
                      <el-form-item label="婚姻状态">
                        <el-select placeholder v-model="livelyForm.status">
                          <el-option label="未婚" value="未婚"></el-option>
                          <el-option label="离异" value="离异"></el-option>
                          <el-option label="丧偶" value="丧偶"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="是否有小孩">
                        <el-select placeholder v-model="livelyForm.child">
                          <el-option label="没有小孩" value="没有小孩"></el-option>
                          <el-option label="有小孩,且住在一起" value="有小孩,且住在一起"></el-option>
                          <el-option label="有小孩,但不住一起" value="有小孩,但不住一起"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="住房情况">
                        <el-select v-model="livelyForm.house">
                          <el-option label="租房" value="租房"></el-option>
                          <el-option label="住公司" value="住公司"></el-option>
                          <el-option label="和家人同住" value="和家人同住"></el-option>
                          <el-option label="已经购房" value="已经购房"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="买车情况">
                        <el-select v-model="livelyForm.car">
                          <el-option label="公司配车" value="公司配车"></el-option>
                          <el-option label="未买车" value="未买车"></el-option>
                          <el-option label="已买私人车" value="已买私人车"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="是否吸烟">
                        <el-select v-model="livelyForm.smoke">
                          <el-option label="不吸烟" value="不吸烟"></el-option>
                          <el-option label="只有应酬才吸烟" value="只有应酬才吸烟"></el-option>
                          <el-option label="偶尔吸烟" value="偶尔吸烟"></el-option>
                          <el-option label="经常吸烟" value="经常吸烟"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="是否喝酒">
                        <el-select v-model="livelyForm.drink">
                          <el-option label="不喝酒" value="不喝酒"></el-option>
                          <el-option label="只有应酬才喝" value="只有应酬才喝"></el-option>
                          <el-option label="偶尔会喝酒" value="偶尔会喝酒"></el-option>
                          <el-option label="经常喝酒" value="经常喝酒"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="健康状况">
                        <el-select v-model="livelyForm.healthy">
                          <el-option label="无疾病" value="无疾病"></el-option>
                          <el-option label="有遗传疾病" value="有遗传疾病"></el-option>
                          <el-option label="有其他疾病" value="有其他疾病"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="宗教信仰">
                        <el-select v-model="livelyForm.religious">
                          <el-option label="无宗教信仰" value="无宗教信仰"></el-option>
                          <el-option label="伊斯兰教" value="伊斯兰教"></el-option>
                          <el-option label="基督教" value="基督教"></el-option>
                          <el-option label="佛教" value="佛教"></el-option>
                          <el-option label="其他宗教" value="其他宗教"></el-option>
                        </el-select>
                      </el-form-item>
                      <div>
                        <el-button :plain="false" @click="saveLivelyForm" type="primary">保存资料</el-button>
                      </div>
                    </el-form>
                  </el-card>
                </el-col>
              </el-row>
            </section>
          </el-tab-pane>
          <el-tab-pane label="我的认证">
            <section>
              <el-row>
                <el-col :offset="1" :span="22">
                  <el-card style="text-align:center">
                    <div slot="header">
                      <span>开始认证</span>
                    </div>
                    <el-row>
                      <el-col :offset="2" :span="3">
                        <img
                          src="../assets/logo.png"
                          style="padding: 30px; max-width: 80px;"
                        />
                      </el-col>
                      <el-col :offset="2" :span="9" style="padding: 0 20px; text-align:left">
                        <h4>实名认证</h4>
                        <span>可以使用更多网站的定制功能，推荐更多诚信的优质客户，与心仪的人发送消息，同时点亮左侧认证图标</span>
                      </el-col>
                      <el-col :span="3" style="padding: 48px;">
                        <el-button>马上认证</el-button>
                      </el-col>
                    </el-row>
                    <el-divider></el-divider>
                    <el-row>
                      <el-col :span="2">
                        <img
                          src="../assets/logo.png"
                          style="padding: 26px; max-width: 80px;"
                        />
                      </el-col>
                      <el-col :offset="1" :span="5" style="padding: 0 20px; text-align:left">
                        <h4>户口认证</h4>
                        <span>认证婚姻信息，点亮左侧图标</span>
                      </el-col>
                      <el-col :span="3" style="padding: 48px 0;">
                        <el-button>马上认证</el-button>
                      </el-col>
                      <el-col :offset="1" :span="1">
                        <hr
                          style="width: 1px; height:120px; border: none; background-color: #d9d9d9;"
                        />
                      </el-col>
                      <el-col :span="2">
                        <img
                          src="../assets/logo.png"
                          style="padding: 26px; max-width: 80px;"
                        />
                      </el-col>
                      <el-col :offset="1" :span="5" style="padding: 0 20px; text-align:left">
                        <h4>学历认证</h4>
                        <span>认证学历信息， 点亮左侧图标</span>
                      </el-col>
                      <el-col :span="3" style="padding: 48px 0;">
                        <el-button>马上认证</el-button>
                      </el-col>
                    </el-row>
                  </el-card>
                </el-col>
              </el-row>
            </section>
          </el-tab-pane>
          <el-tab-pane label="我的爱好">
            <section>
              <el-row>
                <el-col :offset="1" :span="22">
                  <el-card style="text-align: center;">
                    <div slot="header">我的爱好</div>
                    <el-col :offset="3" :span="20">
                      <el-form
                        :model="hobbyForm"
                        label-width="80px"
                        ref="hobbyForm"
                        style="margin-top:16px; text-align:left"
                      >
                        <el-form-item label="兴趣话题">
                          <el-checkbox-group v-model="hobbyForm.topic">
                            <el-checkbox-button label="心理学" name="topic"></el-checkbox-button>
                            <el-checkbox-button label="计算机" name="topic"></el-checkbox-button>
                            <el-checkbox-button label="艺术" name="topic"></el-checkbox-button>
                            <el-checkbox-button label="历史" name="topic"></el-checkbox-button>
                            <el-checkbox-button label="自然" name="topic"></el-checkbox-button>
                            <el-checkbox-button label="经济" name="topic"></el-checkbox-button>
                            <el-checkbox-button label="社会" name="topic"></el-checkbox-button>
                          </el-checkbox-group>
                        </el-form-item>
                        <el-form-item label="体育运动">
                          <el-checkbox-group v-model="hobbyForm.sport">
                            <el-checkbox-button label="健美操" name="sport"></el-checkbox-button>
                            <el-checkbox-button label="游泳" name="sport"></el-checkbox-button>
                            <el-checkbox-button label="自行车" name="sport"></el-checkbox-button>
                            <el-checkbox-button label="跑步" name="sport"></el-checkbox-button>
                            <el-checkbox-button label="瑜伽" name="sport"></el-checkbox-button>
                            <el-checkbox-button label="健身房" name="sport"></el-checkbox-button>
                          </el-checkbox-group>
                        </el-form-item>
                        <el-form-item label="球类运动">
                          <el-checkbox-group v-model="hobbyForm.ballGame">
                            <el-checkbox-button label="足球" name="ballGame"></el-checkbox-button>
                            <el-checkbox-button label="乒乓球" name="ballGame"></el-checkbox-button>
                            <el-checkbox-button label="羽毛球" name="ballGame"></el-checkbox-button>
                            <el-checkbox-button label="高尔夫" name="ballGame"></el-checkbox-button>
                            <el-checkbox-button label="网球" name="ballGame"></el-checkbox-button>
                            <el-checkbox-button label="篮球" name="ballGame"></el-checkbox-button>
                            <el-checkbox-button label="排球" name="ballGame"></el-checkbox-button>
                          </el-checkbox-group>
                        </el-form-item>
                        <el-form-item label="休闲娱乐">
                          <el-checkbox-group v-model="hobbyForm.leisure">
                            <el-checkbox-button label="读书" name="leisure"></el-checkbox-button>
                            <el-checkbox-button label="音乐" name="leisure"></el-checkbox-button>
                            <el-checkbox-button label="电影" name="leisure"></el-checkbox-button>
                            <el-checkbox-button label="旅游" name="leisure"></el-checkbox-button>
                            <el-checkbox-button label="摄影" name="leisure"></el-checkbox-button>
                            <el-checkbox-button label="游戏" name="leisure"></el-checkbox-button>
                            <el-checkbox-button label="宠物" name="leisure"></el-checkbox-button>
                            <el-checkbox-button label="收藏" name="leisure"></el-checkbox-button>
                          </el-checkbox-group>
                          <el-checkbox-group v-model="hobbyForm.leisure">
                            <el-checkbox-button label="KTV/酒吧" name="leisure"></el-checkbox-button>
                            <el-checkbox-button label="美术/书法" name="leisure"></el-checkbox-button>
                          </el-checkbox-group>
                        </el-form-item>
                        <el-form-item label="饮食偏好">
                          <el-checkbox-group v-model="hobbyForm.diet">
                            <el-checkbox-button label="中餐" name="diet"></el-checkbox-button>
                            <el-checkbox-button label="西餐" name="diet"></el-checkbox-button>
                            <el-checkbox-button label="日料" name="diet"></el-checkbox-button>
                            <el-checkbox-button label="韩国料理" name="diet"></el-checkbox-button>
                            <el-checkbox-button label="小吃" name="diet"></el-checkbox-button>
                            <el-checkbox-button label="烧烤" name="diet"></el-checkbox-button>
                            <el-checkbox-button label="火锅" name="diet"></el-checkbox-button>
                            <el-checkbox-button label="海鲜" name="diet"></el-checkbox-button>
                          </el-checkbox-group>
                          <el-checkbox-group v-model="hobbyForm.diet">
                            <el-checkbox-button label="碳酸饮料" name="diet"></el-checkbox-button>
                            <el-checkbox-button label="蔬果汁" name="diet"></el-checkbox-button>
                            <el-checkbox-button label="酒精饮料" name="diet"></el-checkbox-button>
                            <el-checkbox-button label="奶制品" name="diet"></el-checkbox-button>
                            <el-checkbox-button label="茶/咖啡" name="diet"></el-checkbox-button>
                            <el-checkbox-button label="纯净水" name="diet"></el-checkbox-button>
                          </el-checkbox-group>
                        </el-form-item>
                      </el-form>
                      <div style="text-align:center; margin-bottom: 20px;">
                        <el-button :plain="false" @click="saveDataForm" type="primary">保存资料</el-button>
                      </div>
                    </el-col>
                  </el-card>
                </el-col>
              </el-row>
            </section>
          </el-tab-pane>
          <el-tab-pane label="我的相册">
            <section>
              <el-row>
                <el-col :offset="1" :span="22">
                  <el-card>
                    <div slot="header" style="text-align:center">
                      <span>我的相册</span>
                      <el-popover
                        style="margin-left: 36px;"
                        placement="top-start"
                        title="上传头像的注意事项"
                        width="200"
                        trigger="hover"
                      >
                        <div>1. 使用清晰的单人正面近照</div>
                        <div>2. 照片为包括本人完整五官的近期照片</div>
                        <div>3. 不能使用涉黄、涉政、公众照、网络照以及含联系方式的照片</div>
                        <el-button size="small" slot="reference">照片上传说明</el-button>
                      </el-popover>
                    </div>
                    <div>
                      <span>我的头像</span>
                      <el-upload
                        :before-upload="beforeAvatarUpload"
                        :on-success="handleAvatarSuccess"
                        :show-file-list="false"
                        action="https://jsonplaceholder.typicode.com/posts/"
                        class="avatar-uploader"
                      >
                        <img :src="imageUrl" class="avatar" v-if="imageUrl" />
                        <i class="el-icon-plus avatar-uploader-icon" v-else></i>
                      </el-upload>
                      <el-divider></el-divider>
                      <div style="padding: 0 0 18px">
                        <span>我的相册</span>
                      </div>
                      <el-upload
                        :on-preview="handlePictureCardPreview"
                        :on-remove="handleRemove"
                        action="https://jsonplaceholder.typicode.com/posts/"
                        list-type="picture-card"
                      >
                        <i class="el-icon-plus"></i>
                      </el-upload>
                      <el-dialog :visible.sync="dialogVisible">
                        <img :src="dialogImageUrl" alt width="100%" />
                      </el-dialog>
                    </div>
                  </el-card>
                </el-col>
              </el-row>
            </section>
          </el-tab-pane>
          <el-tab-pane label="择偶意向">
            <section>
              <el-row>
                <el-col :offset="1" :span="22">
                  <el-card style="text-align:center">
                    <div slot="header">
                      <span>择偶意向</span>
                    </div>
                    <el-form
                      :inline="true"
                      :model="livelyForm"
                      label-width="100px"
                      ref="conditionForm"
                      style="margin-top:16px"
                    >
                      <el-form-item label="年龄">
                        <el-select v-model="conditionForm.age">
                          <el-option label="测试" value="0"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="身高">
                        <el-select v-model="conditionForm.height">
                          <el-option label="测试" value="0"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="月薪">
                        <el-select v-model="conditionForm.salary">
                          <el-option
                            :key="item.value"
                            :label="item.label"
                            :value="item.value"
                            v-for="item in salaryOptions"
                          ></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="学历">
                        <el-select v-model="conditionForm.degree">
                          <el-option
                            :key="item.value"
                            :label="item.label"
                            :value="item.value"
                            v-for="item in degreeOptions"
                          ></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="工作城市">
                        <div id style="text-align: left;">
                          <el-cascader
                            :options="cityOptions"
                            size="large"
                            v-model="conditionForm.workAddress"
                          ></el-cascader>
                        </div>
                      </el-form-item>
                      <el-form-item label="户籍所在地">
                        <div style="text-align: left;">
                          <el-cascader
                            :options="cityOptions"
                            size="large"
                            v-model="conditionForm.status"
                          ></el-cascader>
                        </div>
                      </el-form-item>
                      <el-form-item label="住房情况">
                        <el-select v-model="conditionForm.house">
                          <el-option label="租房" value="0"></el-option>
                          <el-option label="住公司" value="1"></el-option>
                          <el-option label="和家人同住" value="2"></el-option>
                          <el-option label="已经购房" value="3"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="买车情况">
                        <el-select v-model="conditionForm.car">
                          <el-option label="公司配车" value="0"></el-option>
                          <el-option label="未买车" value="1"></el-option>
                          <el-option label="已买私人车" value="2"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="是否吸烟">
                        <el-select v-model="conditionForm.smoke">
                          <el-option label="不吸烟" value="0"></el-option>
                          <el-option label="只有应酬才吸烟" value="1"></el-option>
                          <el-option label="偶尔吸烟" value="2"></el-option>
                          <el-option label="经常吸烟" value="3"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="是否喝酒">
                        <el-select v-model="conditionForm.drink">
                          <el-option label="不喝酒" value="0"></el-option>
                          <el-option label="只有应酬才喝" value="1"></el-option>
                          <el-option label="偶尔会喝酒" value="2"></el-option>
                          <el-option label="经常喝酒" value="3"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="婚姻状况">
                        <el-select v-model="conditionForm.drink">
                          <el-option label="未婚" value="0"></el-option>
                          <el-option label="离异" value="1"></el-option>
                          <el-option label="丧偶" value="2"></el-option>
                          <el-option label="都可以" value="3"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="是否带小孩">
                        <el-select v-model="conditionForm.drink">
                          <el-option label="没有小孩" value="0"></el-option>
                          <el-option label="小孩不住一起" value="1"></el-option>
                          <el-option label="小孩住一起" value="2"></el-option>
                          <el-option label="都可以" value="3"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="何时结婚">
                        <el-select v-model="conditionForm.drink">
                          <el-option label="无所谓" value="0"></el-option>
                          <el-option label="一年内结婚" value="2"></el-option>
                          <el-option label="1-3年结婚" value="1"></el-option>
                          <el-option label="3-5年结婚" value="1"></el-option>
                          <el-option label="5年以后结婚" value="1"></el-option>
                        </el-select>
                      </el-form-item>
                      <el-form-item label="是否有照片">
                        <el-select v-model="conditionForm.drink">
                          <el-option label="无所谓" value="0"></el-option>
                          <el-option label="有照片" value="1"></el-option>
                        </el-select>
                      </el-form-item>
                      <div>
                        <el-button :plain="false" @click="saveIntentionForm" type="primary">保存资料</el-button>
                      </div>
                    </el-form>
                  </el-card>
                </el-col>
              </el-row>
            </section>
          </el-tab-pane>
          <el-tab-pane label="权限设置">
            <section>
              <el-row>
                <el-col :offset="1" :span="22">
                  <el-card>
                    <div slot="header" style="text-align:center">个人设置</div>
                    <h4>谁可以看我的资料</h4>
                    <div>
                      <el-radio border label="1" v-model="radio">所有人</el-radio>
                      <el-radio border label="2" v-model="radio">只有认证用户</el-radio>
                      <el-radio border label="3" v-model="radio">符合择偶条件的认证用户</el-radio>
                    </div>
                    <el-divider></el-divider>
                    <h4>谁可以查看我的联系方式</h4>
                    <div>
                      <el-radio border label="1" v-model="radio1">所有人</el-radio>
                      <el-radio border label="2" v-model="radio1">只有认证用户</el-radio>
                      <el-radio border label="3" v-model="radio1">符合择偶条件的认证用户</el-radio>
                    </div>
                    <el-divider></el-divider>
                    <h4>我的恋爱状态</h4>
                    <div>
                      <el-radio border label="1" v-model="radio2">寻觅中</el-radio>
                      <el-radio border label="2" v-model="radio2">约会中</el-radio>
                      <el-radio border label="3" v-model="radio2">热恋中</el-radio>
                      <el-radio border label="4" v-model="radio2">我结婚啦</el-radio>
                    </div>
                  </el-card>
                </el-col>
              </el-row>
            </section>
          </el-tab-pane>
          <el-tab-pane label="账号安全">
            <section>
              <el-row>
                <el-col :offset="1" :span="22">
                  <el-card>
                    <div slot="header" style="text-align:center">个人设置</div>
                    <h4>谁可以看我的资料</h4>
                    <div>
                      <el-radio border label="1" v-model="radio">所有人</el-radio>
                      <el-radio border label="2" v-model="radio">只有认证用户</el-radio>
                      <el-radio border label="3" v-model="radio">符合择偶条件的认证用户</el-radio>
                    </div>
                    <el-divider></el-divider>
                    <h4>谁可以查看我的联系方式</h4>
                    <div>
                      <el-radio border label="1" v-model="radio1">所有人</el-radio>
                      <el-radio border label="2" v-model="radio1">只有认证用户</el-radio>
                      <el-radio border label="3" v-model="radio1">符合择偶条件的认证用户</el-radio>
                    </div>
                    <el-divider></el-divider>
                    <h4>我的恋爱状态</h4>
                    <div>
                      <el-radio border label="1" v-model="radio2">寻觅中</el-radio>
                      <el-radio border label="2" v-model="radio2">约会中</el-radio>
                      <el-radio border label="3" v-model="radio2">热恋中</el-radio>
                      <el-radio border label="4" v-model="radio2">我结婚啦</el-radio>
                    </div>
                  </el-card>
                </el-col>
              </el-row>
            </section>
          </el-tab-pane>
          <el-tab-pane label="账号设置">
            <section>
              <el-row>
                <el-col :offset="1" :span="22">
                  <el-card shadow="hover">
                    <div slot="header" style="text-align:center">修改密码</div>
                    <div style="padding: 10px 64px;">
                      <el-steps
                        :active="activeStep"
                        finish-status="success"
                        process-status="finish"
                      >
                        <el-step icon="el-icon-position" title="手机验证"></el-step>
                        <el-step icon="el-icon-unlock" title="修改密码"></el-step>
                        <el-step icon title="完成"></el-step>
                      </el-steps>
                    </div>
                    <el-row justify="center" type="flex">
                      <el-form
                        :model="passwordForm"
                        label-width="100px"
                        ref="passwordForm"
                        style="margin: 16px 0;"
                        v-if="activeStep === 0"
                        :rules="rules"
                      >
                        <el-form-item label="手机号" style="margin-top: 20px;">
                          {{passwordForm.phone.substring(0, 3) + "****" + passwordForm.phone.substring(passwordForm.phone.length-4, passwordForm.phone.length)}}
                          <el-button v-model.number="passwordForm.phone" @click="sendCode(passwordForm)" :style="{ marginLeft: '20px' }">发送验证码</el-button>
                        </el-form-item>
                        <el-form-item label="验证码" prop="verCode">
                          <el-input v-model.number="passwordForm.verCode"></el-input>
                        </el-form-item>
                        <div align="center">
                          <el-button @click="nextStep1('passwordForm')" style="margin-top: 12px;">下一步</el-button>

                        </div>
                      </el-form>
                      <el-form
                        :model="passwordForm"
                        label-width="100px"
                        ref="passwordForm"
                        style="margin: 16px 0;"
                        v-else-if="activeStep === 1"
                        :rules="rules"
                      >
                        <el-form-item label="新密码" style="margin-top: 20px;" prop="newPassword">
                          <el-input v-model="passwordForm.newPassword"></el-input>
                        </el-form-item>
                        <el-form-item label="确认密码" prop="newPassword2">
                          <el-input v-model="passwordForm.newPassword2"></el-input>
                        </el-form-item>
                        <div align="center">
                          <el-button @click="nextStep2('passwordForm')" style="margin-top: 12px;">下一步</el-button>
                        </div>
                      </el-form>
                      <el-form :model="passwordForm" label-width="100px" ref="passwordForm" v-else>
                        <el-alert
                          center
                          show-icon
                          style="padding: 10px 30px; margin: 24px 0;"
                          title="密码修改成功"
                          type="success"
                        ></el-alert>
                        <div align="center">
                          <el-button @click="nextStep3" style="margin-top: 12px;">完成</el-button>
                        </div>
                      </el-form>
                    </el-row>
                  </el-card>
                </el-col>
              </el-row>
            </section>
          </el-tab-pane>
        </el-tabs>
      </el-row>
    </el-main>
  </el-container>
</template>

<script>
import { regionData } from 'element-china-area-data'
import store from '../store'
export default {
  name: 'Edit',
  data () {
    var checkCode = (rule, value, callback) => {
      if (!value) {
        return callback(new Error('验证码不能为空'))
      }
      setTimeout(() => {
        if (!Number.isInteger(value)) {
          callback(new Error('请输入数字'))
        } else {
          if (value !== this.passwordForm.code) {
            callback(new Error('请输入正确的验证码'))
          } else {
            callback()
          }
        }
      }, 1000)
    }
    var checkPass = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请输入密码'))
      } else {
        if (this.passwordForm.newPassword2 !== '') {
          this.$refs.passwordForm.validateField('newPassword2')
        }
        callback()
      }
    }
    var checkPass2 = (rule, value, callback) => {
      if (value === '') {
        callback(new Error('请再次输入密码'))
      } else if (value !== this.passwordForm.newPassword) {
        callback(new Error('两次输入密码不一致!'))
      } else {
        callback()
      }
    }
    return {
      sharedState: store.state,
      activeStep: 0,
      radio: '',
      radio1: '',
      radio2: '',
      imageUrl: '',
      dialogImageUrl: '',
      modifyDialog: false,
      cityOptions: regionData,
      heightRange: Array(100).keys(),
      userAvatar: undefined,
      personalForm: {
        username: '',
        workPlace: [],
        salary: '',
        height: '',
        degree: '',
        job: ''
      },
      hobbyForm: {
        topic: [],
        sport: [],
        ballGame: [],
        leisure: [],
        diet: []
      },
      livelyForm: {
        status: '',
        child: '',
        religious: '',
        healthy: '',
        house: '',
        car: '',
        smoke: '',
        drink: ''
      },
      conditionForm: {
        age: '',
        height: '',
        salary: '',
        degree: '',
        status: '',
        workAddress: '',
        native: '',
        kid: '',
        drink: '',
        smoke: '',
        pic: '',
        marryTime: ''
      },
      passwordForm: {
        phone: '',
        verCode: '',
        code: '',
        newPassword: '',
        newPassword2: ''
      },
      contactForm: {
        QQ: '',
        wechat: ''
      },
      salaryOptions: [
        {
          value: '3000元以下',
          label: '3000元以下'
        },
        {
          value: '3001~6000元',
          label: '3001~6000元'
        },
        {
          value: '6001~12000元',
          label: '6001~12000元'
        },
        {
          value: '12001~24000元',
          label: '12001~24000元'
        },
        {
          value: '24001~50000元',
          label: '24001~50000元'
        },
        {
          value: '50000元以上',
          label: '50000元以上'
        }
      ],
      degreeOptions: [
        {
          value: '中专及以下',
          label: '中专及以下'
        },
        {
          value: '大专',
          label: '大专'
        },
        {
          value: '本科',
          label: '本科'
        },
        {
          value: '硕士',
          label: '硕士'
        },
        {
          value: '博士',
          label: '博士'
        }
      ],
      rules: {
        newPassword: [
          { validator: checkPass, trigger: 'blur' }
          // { min: 6, message: '密码长度至少为6位', trigger: 'blur' }
        ],
        newPassword2: [
          { validator: checkPass2, trigger: 'blur' }
        ],
        verCode: [
          { validator: checkCode, trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    getUser (id) {
      const path = `/users/${id}`
      this.$axios.get(path)
        .then((response) => {
          this.personalForm.username = response.data.name
          this.passwordForm.phone = response.data.phone
          console.log(this.personalForm.username)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error)
        })
    },
    savePersonalForm () {
      // eslint-disable-next-line camelcase
      const user_id = this.sharedState.user_id
      // eslint-disable-next-line camelcase
      const path = `/users/personal/${user_id}`
      const payload = {
        username: this.personalForm.username,
        salary: this.personalForm.salary,
        degree: this.personalForm.degree,
        height: this.personalForm.height
      }
      this.$axios.put(path, payload)
        .then((response) => {
          // handle success
          this.$toasted.success('Successed modify your profile.', { icon: 'fingerprint' })
          this.$router.push({
            name: 'Profile',
            params: { id: user_id }
          })
        })
        .catch((error) => {
          // handle error
          console.log(error.response.data)
        })
    },
    saveLivelyForm () {
      // eslint-disable-next-line camelcase
      const user_id = this.sharedState.user_id
      // eslint-disable-next-line camelcase
      const path = `/users/lively/${user_id}`
      const payload = {
        marital_status: this.livelyForm.status,
        children: this.livelyForm.child,
        house: this.livelyForm.house,
        car: this.livelyForm.car,
        smoke: this.livelyForm.smoke,
        drink: this.livelyForm.drink,
        health: this.livelyForm.healthy,
        religion: this.livelyForm.religious
      }
      this.$axios.put(path, payload)
        .then((response) => {
          // handle success
          this.$toasted.success('Successed modify your profile.', { icon: 'fingerprint' })
          this.$router.push({
            name: 'Profile',
            params: { id: user_id }
          })
        })
        .catch((error) => {
          // handle error
          console.log(error.response.data)
        })
    },
    sendCode (formName) {
      // eslint-disable-next-line standard/object-curly-even-spacing
      const path = 'http://localhost:5001/v1/verify'
      const payload = {
        phone: Number(this.passwordForm.phone)
      }
      this.$axios.post(path, payload)
        .then((response) => {
          console.log(response.data)
          if (response.data.error_code === 0) {
            this.passwordForm.code = response.data.code
            this.$message({
              showClose: true,
              message: '短信已发送，请注意查收',
              type: 'info',
              duration: 5000,
              center: true
            })
          }
        })
        .catch((error) => {
          console.log(error.response)
          if (error.response.data.error_code === 1002) {
            this.$message({
              showClose: true,
              message: '短信发送过于频繁，请稍后再试',
              type: 'warning',
              duration: 5000,
              center: true
            })
          } else if (error.response.data.error_code === 1003) {
            this.$message({
              showClose: true,
              message: '该手机号不存在，请输入正确的手机号',
              type: 'warning',
              duration: 5000,
              center: true
            })
          } else if (error.response.data.error_code === 999) {
            this.$message({
              showClose: true,
              message: '短信功能异常，请联系客服',
              type: 'warning',
              duration: 5000,
              center: true
            })
          }
        })
    },
    handleAvatarSuccess (res, file) {
      this.imageUrl = URL.createObjectURL(file.raw)
    },
    beforeAvatarUpload (file) {
      const isJPG = file.type === 'image/jpeg'
      const isLt2M = file.size / 1024 / 1024 < 2

      if (!isJPG) {
        this.$message.error('上传头像图片只能是 JPG 格式!')
      }
      if (!isLt2M) {
        this.$message.error('上传头像图片大小不能超过 2MB!')
      }
      return isJPG && isLt2M
    },
    handleUploaded (resp) {
      this.userAvatar = resp.relative_url
    },
    handleRemove (file, fileList) {
      console.log(file, fileList)
    },
    handlePictureCardPreview (file) {
      this.dialogImageUrl = file.url
      this.modifyDialog = true
    },
    nextStep1 (formName) {
      this.$refs[formName].validateField('verCode', (valid) => {
        console.log(valid)
        if (valid === '') {
          this.$message({
            showClose: true,
            message: '验证成功，请填写新密码',
            type: 'success',
            center: true
          })
          if (this.activeStep++ > 2) this.activeStep = 0
        } else {
          this.$message({
            showClose: true,
            message: '验证码错误，请输入正确的验证码',
            type: 'error',
            center: true
          })
        }
      })
    },
    nextStep2 (formName) {
      console.log(formName)
      this.$refs[formName].validateField(['newPassword', 'newPassword2'], (valid) => {
        const path = '/reset-pw'
        const payload = {
        //   phone: Number(this.codeForm.phone),
          phone: 13823332664,
          password: this.passwordForm.newPassword
        }
        this.$axios.post(path, payload)
          .then((response) => {
            this.$message({
              showClose: true,
              message: '密码修改成功',
              type: 'success',
              center: true
            })
            // 验证成功
            if (this.activeStep++ > 2) this.activeStep = 0
          })
          .catch((error) => {
            if (error) {
              this.$message({
                showClose: true,
                message: '未知错误',
                type: 'info',
                duration: 5000,
                center: true
              })
            }
          })
      })
    },
    nextStep3 () {
      if (this.activeStep++ > 2) this.activeStep = 0
    }
  },
  created () {
    // eslint-disable-next-line camelcase
    const user_id = this.sharedState.user_id
    this.getUser(user_id)
  }
}
</script>

<style scoped>
  .editMain {
    max-width: 1160px;
    margin: 0 auto;
  }
  .avatar-uploader .el-upload {
    border: 1px dashed #d9d9d9;
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    margin-top: 20px;
    width: 178px;
    height: 178px;
    line-height: 178px;
    text-align: center;
  }
  .avatar-uploader .el-upload:hover {
    border-color: #409eff;
  }
  .avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
  }
  .avatar {
    width: 178px;
    height: 178px;
    display: block;
  }
</style>

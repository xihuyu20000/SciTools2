<template>
  <div>
    <el-collapse v-model="activeNames">
      <el-collapse-item title="词云" name="1">
        <el-row :gutter="12">
          <el-col v-for="i in 6" :span="4" :key="i">
            <el-card shadow="hover">
              鼠标悬浮时显示
            </el-card>
          </el-col>
        </el-row>
      </el-collapse-item>
      <el-collapse-item title="折线图" name="2">
        <el-row :gutter="12">
          <el-col :span="4">
            <el-card shadow="hover">
              <router-link :to="{ path: '/graph/line/echartsLine' }">历年发文量</router-link>
            </el-card>
          </el-col>
          <el-col v-for="i in 5" :span="4" :key="i">
            <el-card shadow="hover">
              鼠标悬浮时显示
            </el-card>
          </el-col>
        </el-row>
      </el-collapse-item>
      <el-collapse-item title="柱状图" name="3">
        <el-row :gutter="12">
          <el-col v-for="i in 6" :span="4" :key="i">
            <el-card shadow="hover">
              鼠标悬浮时显示
            </el-card>
          </el-col>
        </el-row>
      </el-collapse-item>
      <el-collapse-item title="饼图" name="4">
        <el-row :gutter="12">
          <el-col v-for="i in 6" :span="4" :key="i">
            <el-card shadow="hover">
              鼠标悬浮时显示
            </el-card>
          </el-col>
        </el-row>
      </el-collapse-item>
      <el-collapse-item title="知识图谱" name="5">
        <el-row :gutter="12">
          <el-col v-for="i in 6" :span="4" :key="i">
            <el-card shadow="hover">
              鼠标悬浮时显示
            </el-card>
          </el-col>
        </el-row>
      </el-collapse-item>
      <el-collapse-item title="表格" name="6">
        <el-row :gutter="12">
          <el-col v-for="i in 6" :span="4" :key="i">
            <el-card shadow="hover">
              鼠标悬浮时显示
            </el-card>
          </el-col>
        </el-row>
      </el-collapse-item>
    </el-collapse>
  </div>
</template>

<script>
export default {
  data() {
    return {}
  },
  mounted: function() {}
}
</script>

<style lang="scss" scoped></style>

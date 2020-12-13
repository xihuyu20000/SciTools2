<template>
  <el-card class="box-card">
    <el-row>
      <el-col :span="24">
        <el-radio-group v-model="filterStyle" @change="changeFilterStyle">
          <el-radio :label="1">条件过滤</el-radio>
          <el-radio :label="2">表达式过滤</el-radio>
        </el-radio-group>
      </el-col>
    </el-row>
    <el-row v-show="isShowConditionFilterBuiler">
      <el-col :span="4">
        条件过滤
        <!-- <el-select clearable placeholder="请选择字段">
          <el-option v-for="item in 10" :key="item" :label="item" :value="item"> </el-option>
        </el-select>
        <el-select clearable placeholder="请选择函数">
          <el-option v-for="item in 10" :key="item" :label="item" :value="item"> </el-option>
        </el-select> -->
      </el-col>
      <el-col :span="18"><el-input type="textarea" :rows="4" placeholder="请输入内容"> </el-input></el-col>
      <el-col :span="2">
        <el-link type="success">语法检查</el-link>
        <el-button>执行过滤</el-button>
      </el-col>
    </el-row>
    <el-row v-show="!isShowConditionFilterBuiler">
      <el-col :span="4">
        表达式过滤
        <!-- <el-select clearable placeholder="请选择字段">
          <el-option v-for="item in 10" :key="item" :label="item" :value="item"> </el-option>
        </el-select>
        <el-select clearable placeholder="请选择函数">
          <el-option v-for="item in 10" :key="item" :label="item" :value="item"> </el-option>
        </el-select> -->
      </el-col>
      <el-col :span="18"><el-input type="textarea" :rows="4" placeholder="请输入内容"> </el-input></el-col>
      <el-col :span="2">
        <el-link type="success">语法检查</el-link>
        <el-button>执行过滤</el-button>
      </el-col>
    </el-row>
  </el-card>
</template>

<script>
export default {
  data() {
    return { filterStyle: 1, isShowConditionFilterBuiler: true }
  },
  methods: {
    changeFilterStyle(v) {
      this.isShowConditionFilterBuiler = v == 1
    }
  }
}
</script>

<style></style>

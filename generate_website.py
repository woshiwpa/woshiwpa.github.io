# this script should be run in Linux/Cygwin. Its path and Url are all divided by forward slash.
import os
import shutil

anMathAssetsFolder = 'D:/Development/AStudioProjs/AnMath/anMath/src/main/assets'
sourceWebPagesFolder = 'D:/Development/git_repo/MFPLang4JVM/docs'
destWebPagesFolder = 'D:/Development/git_repo/woshiwpa.github.io/MFPLang'

styleStr = '''<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  font-family: "Lato", sans-serif;
}

.sidenav {
  height: 100%;
  width: 200px;
  position: fixed;
  z-index: 1;
  top: 0;
  left: 0;
  background-color: #111;
  overflow-x: hidden;
  padding-top: 20px;
}

.sidenav a {
  padding: 6px 8px 6px 16px;
  text-decoration: none;
  /*font-size: 16px;*/
  color: #f1f111;
  display: block;
}

.sidenav a:hover {
  color: #f111f1;
}

.main {
  margin-left: 200px; /* Same as the width of the sidenav */
  /*font-size: 28px;  Increased text to enable scrolling */
  padding: 0px 10px;
}

@media screen and (max-height: 450px) {
  .sidenav {padding-top: 15px;}
  .sidenav a {font-size: 18px;}
}
</style>
'''
endOfFileStr = '''</div>
   
</body>
</html>'''

class MFPWebSiteNode:
    def __init__(self, name: str, pageFilePath: str, parent):
        self.name = name
        self.pageFilePath = pageFilePath
        self.parent = parent
        self.children = []
        if parent is not None:
            # hook itself to parent.
            parent.__addChild(self)
            self.level = parent.level + 1
        else:
            self.level = 0
        self.upperLevelStr = ''.join(['../' for idx in range(self.pageFilePath.count('/'))])
        fontStr = '<p style="font-size:{0}px;">'.format(18 - 3*self.level)
        self.myLine = '\t' + fontStr + '<a href="' + self.pageFilePath + '">' + self.name + '</a></p>\n'
    
    def __addChild(self, childNode):
        self.children.append(childNode)
        
    def outputSideBar(webpageNode, lang):
        otherLang = 'en' if lang != 'en' else 'zh-CN'
        otherLangRefStr = '<p style="font-size:18px;"><a href="../' + otherLang + '/MFPIndex.html">' + ('[English Version]' if otherLang == 'en' else '【中文版】') + '</a></p>\n'
        totalLines = webpageNode.myLine
        for child in webpageNode.children:
            totalLines += child.myLine

        thisLevelNode = webpageNode
        thisParentNode = webpageNode.parent
        while thisParentNode is not None:
            totalLinesOld = totalLines
            totalLines = ''
            for child in thisParentNode.children:
                if child == thisLevelNode:
                    childLine = totalLinesOld
                else:
                    childLine = child.myLine
                totalLines += childLine
            totalLines = thisParentNode.myLine + totalLines
            thisLevelNode = thisParentNode
            thisParentNode = thisLevelNode.parent
        totalLines += '<p/><p/><p/>' # add 3 more lines to avoid x-scrolling bar covers sidebar items.
        return otherLangRefStr + totalLines
                
for lang in ['en', 'zh-CN']:
    if os.path.exists(destWebPagesFolder + '/' + lang + '/'):
        shutil.rmtree(destWebPagesFolder + '/' + lang + '/')
    shutil.copy(anMathAssetsFolder + '/' + lang + '/whats_new.html', sourceWebPagesFolder + '/' + lang + '/whats_new.html')
    shutil.copytree(anMathAssetsFolder + '/' + lang + '/FunctionInfo/', sourceWebPagesFolder + '/' + lang + '/FunctionInfo/', dirs_exist_ok=True)
    shutil.copytree(anMathAssetsFolder + '/' + lang + '/HowtoInfo/', sourceWebPagesFolder + '/' + lang + '/HowtoInfo/', dirs_exist_ok=True)
    shutil.copytree(anMathAssetsFolder + '/' + lang + '/LanguageInfo/', sourceWebPagesFolder + '/' + lang + '/LanguageInfo/', dirs_exist_ok=True)
    shutil.copytree(sourceWebPagesFolder + '/' + lang + '/', destWebPagesFolder + '/' + lang + '/')

    indexName = 'Introduction' if lang != 'zh-CN' else 'MFP语言和可编程科学计算器'

    languageName = 'MFP language introduction' if lang != 'zh-CN' else 'MFP语言简介'
    operatorsName = 'operators'
    functionStatementName = 'function'
    variableStatementName = 'variable'
    ifStatementName = 'if'
    loopStatementName = 'while do for'
    breakStatementName = 'break continue'
    selectStatementName = 'select'
    tryStatementName = 'try catch'
    classStatementName = 'class'
    callStatementName = 'call'
    citingspaceStatementName = 'citingspace'
    helpStatementName = 'help'
    compulsoryLinkAnnotationName = '@compulsory_link'
    executionEntryAnnotationName = '@execution_entry'
    buildAssetAnnotationName = '@build_asset'

    functionIndexName = 'MFP functions' if lang != 'zh-CN' else 'MFP函数'
    allFunctionsName = 'all functions' if lang != 'zh-CN' else '所有函数'
    integerFunctionsName = 'integer operation' if lang != 'zh-CN' else '整数操作函数'
    logicFunctionsName = 'logic functions' if lang != 'zh-CN' else '逻辑函数'
    statisticFunctionsName = 'statistic and stochastic' if lang != 'zh-CN' else '统计和随机函数'
    trigononmetricFunctionsName = 'trigononmetric functions' if lang != 'zh-CN' else '三角函数'
    exponentialFunctionsName = 'exponential functions' if lang != 'zh-CN' else '指数函数'
    complexFunctionsName = 'complex number' if lang != 'zh-CN' else '复数函数'
    systemFunctionsName = 'system functions' if lang != 'zh-CN' else '系统函数'
    arrayFunctionsName = 'array or matrix' if lang != 'zh-CN' else '数组和矩阵函数'
    graphicFunctionsName = 'graphic functions' if lang != 'zh-CN' else '绘图函数'
    expressionFunctionsName = 'expression and calculus' if lang != 'zh-CN' else '表达式和微积分函数'
    stringFunctionsName = 'string functions' if lang != 'zh-CN' else '字符串函数'
    hyperbolicFunctionsName = 'hyperbolic trigononmetric' if lang != 'zh-CN' else '双曲三角函数'
    sortingFunctionsName = 'sorting functions' if lang != 'zh-CN' else '排序函数'
    polynomialFunctionsName = 'polynomial' if lang != 'zh-CN' else '多项式函数'
    signalFunctionsName = 'signal processing' if lang != 'zh-CN' else '信号处理函数'
    fileFunctionsName = 'file operation' if lang != 'zh-CN' else '文件操作函数'
    timedateFunctionsName = 'time and date' if lang != 'zh-CN' else '时间和日期函数'
    displayFunctionsName = 'graphic display' if lang != 'zh-CN' else '显示函数'
    multimediaFunctionsName = 'multimedia functions' if lang != 'zh-CN' else '多媒体函数'
    datastructureFunctionsName = 'data structure' if lang != 'zh-CN' else '数据结构函数'
    exdataFunctionsName = 'data interchange format' if lang != 'zh-CN' else '数据交换文件格式函数'
    platformFunctionsName = 'platform and hardware' if lang != 'zh-CN' else '平台和硬件函数'
    parallelFunctionsName = 'parallel computing' if lang != 'zh-CN' else '并行计算函数'
    rtcmmediaFunctionsName = 'RTC multimedia' if lang != 'zh-CN' else 'RTC多媒体函数'
    reflectionFunctionsName = 'reflection' if lang != 'zh-CN' else '反射函数'
    mfpcompilingFunctionsName = 'MFP compiling' if lang != 'zh-CN' else 'MFP编译函数'
    othersFunctionsName = 'others' if lang != 'zh-CN' else '其它函数'

    deployUserFunctionsTopicName = 'deploy user functions' if lang != 'zh-CN' else '部署用户自定义函数'
    useMFPAnLibTopicName = 'call MFP in your app' if lang != 'zh-CN' else '在您的应用中调用MFP'
    buildAPKTopicName = 'build Android APK' if lang != 'zh-CN' else '创建安卓安装包'

    gameTopicName = 'game programming' if lang != 'zh-CN' else '小游戏的开发'
    gameFundamentalTopicName = 'game fundametnal' if lang != 'zh-CN' else '小游戏基础'
    processImgSndTopicName = 'process image/sound' if lang != 'zh-CN' else '处理图像和声音'
    drawTextTopicName = 'draw text' if lang != 'zh-CN' else '绘制文字'
    hungrysnakeTopicName = 'a hungry snake game' if lang != 'zh-CN' else '一个贪吃蛇游戏'
    gemcrushTopicName = 'a gem crush game' if lang != 'zh-CN' else '一个销宝石游戏'
    rabbitjumpingTopicName = 'a rabbit jumping game' if lang != 'zh-CN' else '一个超级小白兔游戏'
    multiplayerTopicName = 'multiple device/player game' if lang != 'zh-CN' else '多设备多玩家游戏'

    chartingTopicName = 'chart plotting' if lang != 'zh-CN' else '绘制图形'
    chartfunctionsTopicName = 'chart plotting functions' if lang != 'zh-CN' else '使用绘图函数'
    charttoolsTopicName = 'chart plotting tools' if lang != 'zh-CN' else '使用绘图工具'

    mathFunctionsTopicName = 'MFP math analysis' if lang != 'zh-CN' else '使用MFP进行数学分析'
    fileOperationTopicName = 'MFP file procession' if lang != 'zh-CN' else '使用MFP处理文件'
    numberStrArrayTopicName = 'number string and array' if lang != 'zh-CN' else '数，字符串和数组'
    timeDateSysTopicName = 'time date and system' if lang != 'zh-CN' else '日期时间和系统相关'

    scpIntroTopicName = 'Introduction of SCP' if lang != 'zh-CN' else '可编程科学计算器介绍'

    # Now build side bar list. Note that the address is always forward slash
    allNodes = set()
    websiteRootNode = MFPWebSiteNode(indexName, 'MFPIndex.html', None)
    allNodes.add(websiteRootNode)
    languageNode = MFPWebSiteNode(languageName, 'LanguageInfo/language.html', websiteRootNode)
    allNodes.add(languageNode)
    functionIndexNode = MFPWebSiteNode(functionIndexName, 'FunctionInfo/functions.html', websiteRootNode)
    allNodes.add(functionIndexNode)
    deployUserFunctionsNode = MFPWebSiteNode(deployUserFunctionsTopicName, 'HowtoInfo/deploy_user_functions.html', websiteRootNode)
    allNodes.add(deployUserFunctionsNode)
    useMFPAnLibTopicNode = MFPWebSiteNode(useMFPAnLibTopicName, 'HowtoInfo/use_mfp_android_lib.html', websiteRootNode)
    allNodes.add(useMFPAnLibTopicNode)
    buildAPKTopicNode = MFPWebSiteNode(buildAPKTopicName, 'HowtoInfo/build_apk.html', websiteRootNode)
    allNodes.add(buildAPKTopicNode)
    gameTopicNode = MFPWebSiteNode(gameTopicName, 'GameProgramming/index.html', websiteRootNode)
    allNodes.add(gameTopicNode)
    chartingTopicNode = MFPWebSiteNode(chartingTopicName, 'ChartPlotting/index.html', websiteRootNode)
    allNodes.add(chartingTopicNode)
    mathFunctionsTopicNode = MFPWebSiteNode(mathFunctionsTopicName, 'MathFunctions/math_functions.html', websiteRootNode)
    allNodes.add(mathFunctionsTopicNode)
    fileOperationTopicNode = MFPWebSiteNode(fileOperationTopicName, 'FileOperation/file_operation.html', websiteRootNode)
    allNodes.add(fileOperationTopicNode)
    numberStrArrayTopicNode = MFPWebSiteNode(numberStrArrayTopicName, 'NumberStrArray/number_str_array.html', websiteRootNode)
    allNodes.add(numberStrArrayTopicNode)
    timeDateSysTopicNode = MFPWebSiteNode(timeDateSysTopicName, 'TimeDateSysFuncs/time_date_sys_functions.html', websiteRootNode)
    allNodes.add(timeDateSysTopicNode)
    scpIntroTopicNode = MFPWebSiteNode(scpIntroTopicName, 'SCPIntro/tutorial_4_scp_users.html', websiteRootNode)
    allNodes.add(scpIntroTopicNode)

    operatorsNode = MFPWebSiteNode(operatorsName, 'LanguageInfo/operators.html', languageNode)
    allNodes.add(operatorsNode)
    functionStatementNode = MFPWebSiteNode(functionStatementName, 'LanguageInfo/function_return_endf.html', languageNode)
    allNodes.add(functionStatementNode)
    variableStatementNode = MFPWebSiteNode(variableStatementName, 'LanguageInfo/variable.html', languageNode)
    allNodes.add(variableStatementNode)
    ifStatementNode = MFPWebSiteNode(ifStatementName, 'LanguageInfo/if_elseif_else_endif.html', languageNode)
    allNodes.add(ifStatementNode)
    loopStatementNode = MFPWebSiteNode(loopStatementName, 'LanguageInfo/while_loop_do_until_for_next.html', languageNode)
    allNodes.add(loopStatementNode)
    breakStatementNode = MFPWebSiteNode(breakStatementName, 'LanguageInfo/break_continue.html', languageNode)
    allNodes.add(breakStatementNode)
    selectStatementNode = MFPWebSiteNode(selectStatementName, 'LanguageInfo/select_case_default_ends.html', languageNode)
    allNodes.add(selectStatementNode)
    tryStatementNode = MFPWebSiteNode(tryStatementName, 'LanguageInfo/try_throw_catch_endtry.html', languageNode)
    allNodes.add(tryStatementNode)
    classStatementNode = MFPWebSiteNode(classStatementName, 'LanguageInfo/class_endclass.html', languageNode)
    allNodes.add(classStatementNode)
    callStatementNode = MFPWebSiteNode(callStatementName, 'LanguageInfo/call_endcall.html', languageNode)
    allNodes.add(callStatementNode)
    citingspaceStatementNode = MFPWebSiteNode(citingspaceStatementName, 'LanguageInfo/citingspace_using.html', languageNode)
    allNodes.add(citingspaceStatementNode)
    helpStatementNode = MFPWebSiteNode(helpStatementName, 'LanguageInfo/help_endh_ATlanguage.html', languageNode)
    allNodes.add(helpStatementNode)
    compulsoryLinkAnnotationNode = MFPWebSiteNode(compulsoryLinkAnnotationName, 'LanguageInfo/ATcompulsory_link.html', languageNode)
    allNodes.add(compulsoryLinkAnnotationNode)
    executionEntryAnnotationNode = MFPWebSiteNode(executionEntryAnnotationName, 'LanguageInfo/ATexecution_entry.html', languageNode)
    allNodes.add(executionEntryAnnotationNode)
    buildAssetAnnotationNode = MFPWebSiteNode(buildAssetAnnotationName, 'LanguageInfo/ATbuild_asset.html', languageNode)
    allNodes.add(buildAssetAnnotationNode)

    allFunctionsNode = MFPWebSiteNode(allFunctionsName, 'FunctionInfo/all.html', functionIndexNode)
    allNodes.add(allFunctionsNode)
    integerFunctionsNode = MFPWebSiteNode(integerFunctionsName, 'FunctionInfo/integer_operation.html', functionIndexNode)
    allNodes.add(integerFunctionsNode)
    logicFunctionsNode = MFPWebSiteNode(logicFunctionsName, 'FunctionInfo/logic.html', functionIndexNode)
    allNodes.add(logicFunctionsNode)
    statisticFunctionsNode = MFPWebSiteNode(statisticFunctionsName, 'FunctionInfo/statistic_and_stochastic.html', functionIndexNode)
    allNodes.add(statisticFunctionsNode)
    trigononmetricFunctionsNode = MFPWebSiteNode(trigononmetricFunctionsName, 'FunctionInfo/trigononmetric.html', functionIndexNode)
    allNodes.add(trigononmetricFunctionsNode)
    exponentialFunctionsNode = MFPWebSiteNode(exponentialFunctionsName, 'FunctionInfo/exponential_and_logarithmic.html', functionIndexNode)
    allNodes.add(exponentialFunctionsNode)
    complexFunctionsNode = MFPWebSiteNode(complexFunctionsName, 'FunctionInfo/complex_number.html', functionIndexNode)
    allNodes.add(complexFunctionsNode)
    systemFunctionsNode = MFPWebSiteNode(systemFunctionsName, 'FunctionInfo/system.html', functionIndexNode)
    allNodes.add(systemFunctionsNode)
    arrayFunctionsNode = MFPWebSiteNode(arrayFunctionsName, 'FunctionInfo/array_or_matrix.html', functionIndexNode)
    allNodes.add(arrayFunctionsNode)
    graphicFunctionsNode = MFPWebSiteNode(graphicFunctionsName, 'FunctionInfo/graphic.html', functionIndexNode)
    allNodes.add(graphicFunctionsNode)
    expressionFunctionsNode = MFPWebSiteNode(expressionFunctionsName, 'FunctionInfo/expression_and_calculus.html', functionIndexNode)
    allNodes.add(expressionFunctionsNode)
    stringFunctionsNode = MFPWebSiteNode(stringFunctionsName, 'FunctionInfo/string.html', functionIndexNode)
    allNodes.add(stringFunctionsNode)
    hyperbolicFunctionsNode = MFPWebSiteNode(hyperbolicFunctionsName, 'FunctionInfo/hyperbolic_trigononmetric.html', functionIndexNode)
    allNodes.add(hyperbolicFunctionsNode)
    sortingFunctionsNode = MFPWebSiteNode(sortingFunctionsName, 'FunctionInfo/sorting.html', functionIndexNode)
    allNodes.add(sortingFunctionsNode)
    polynomialFunctionsNode = MFPWebSiteNode(polynomialFunctionsName, 'FunctionInfo/polynomial.html', functionIndexNode)
    allNodes.add(polynomialFunctionsNode)
    signalFunctionsNode = MFPWebSiteNode(signalFunctionsName, 'FunctionInfo/signal_proc.html', functionIndexNode)
    allNodes.add(signalFunctionsNode)
    fileFunctionsNode = MFPWebSiteNode(fileFunctionsName, 'FunctionInfo/file.html', functionIndexNode)
    allNodes.add(fileFunctionsNode)
    timedateFunctionsNode = MFPWebSiteNode(timedateFunctionsName, 'FunctionInfo/time_and_date.html', functionIndexNode)
    allNodes.add(timedateFunctionsNode)
    displayFunctionsNode = MFPWebSiteNode(displayFunctionsName, 'FunctionInfo/gdi.html', functionIndexNode)
    allNodes.add(displayFunctionsNode)
    multimediaFunctionsNode = MFPWebSiteNode(multimediaFunctionsName, 'FunctionInfo/multimedia.html', functionIndexNode)
    allNodes.add(multimediaFunctionsNode)
    datastructureFunctionsNode = MFPWebSiteNode(datastructureFunctionsName, 'FunctionInfo/datastruct.html', functionIndexNode)
    allNodes.add(datastructureFunctionsNode)
    exdataFunctionsNode = MFPWebSiteNode(exdataFunctionsName, 'FunctionInfo/exdata.html', functionIndexNode)
    allNodes.add(exdataFunctionsNode)
    platformFunctionsNode = MFPWebSiteNode(platformFunctionsName, 'FunctionInfo/platform_hardware.html', functionIndexNode)
    allNodes.add(platformFunctionsNode)
    parallelFunctionsNode = MFPWebSiteNode(parallelFunctionsName, 'FunctionInfo/parallel.html', functionIndexNode)
    allNodes.add(parallelFunctionsNode)
    rtcmmediaFunctionsNode = MFPWebSiteNode(rtcmmediaFunctionsName, 'FunctionInfo/rtcmmedia.html', functionIndexNode)
    allNodes.add(rtcmmediaFunctionsNode)
    reflectionFunctionsNode = MFPWebSiteNode(reflectionFunctionsName, 'FunctionInfo/reflection.html', functionIndexNode)
    allNodes.add(reflectionFunctionsNode)
    mfpcompilingFunctionsNode = MFPWebSiteNode(mfpcompilingFunctionsName, 'FunctionInfo/mfpcompiler.html', functionIndexNode)
    allNodes.add(mfpcompilingFunctionsNode)
    othersFunctionsNode = MFPWebSiteNode(othersFunctionsName, 'FunctionInfo/others.html', functionIndexNode)
    allNodes.add(othersFunctionsNode)

    gameFundamentalTopicNode = MFPWebSiteNode(gameFundamentalTopicName, 'GameProgramming/game_fundamental.html', gameTopicNode)
    allNodes.add(gameFundamentalTopicNode)
    processImgSndTopicNode = MFPWebSiteNode(processImgSndTopicName, 'GameProgramming/process_img_sound.html', gameTopicNode)
    allNodes.add(processImgSndTopicNode)
    drawTextTopicNode = MFPWebSiteNode(drawTextTopicName, 'GameProgramming/draw_text.html', gameTopicNode)
    allNodes.add(drawTextTopicNode)
    hungrysnakeTopicNode = MFPWebSiteNode(hungrysnakeTopicName, 'GameProgramming/hungry_snake.html', gameTopicNode)
    allNodes.add(hungrysnakeTopicNode)
    gemcrushTopicNode = MFPWebSiteNode(gemcrushTopicName, 'GameProgramming/gem_gem.html', gameTopicNode)
    allNodes.add(gemcrushTopicNode)
    rabbitjumpingTopicNode = MFPWebSiteNode(rabbitjumpingTopicName, 'GameProgramming/super_rabbit.html', gameTopicNode)
    allNodes.add(rabbitjumpingTopicNode)
    multiplayerTopicNode = MFPWebSiteNode(multiplayerTopicName, 'GameProgramming/multi_player_hungry_snake.html', gameTopicNode)
    allNodes.add(multiplayerTopicNode)

    chartfunctionsTopicNode = MFPWebSiteNode(chartfunctionsTopicName, 'ChartPlotting/MFP_graphing_functions.html', chartingTopicNode)
    allNodes.add(chartfunctionsTopicNode)
    charttoolsTopicNode = MFPWebSiteNode(charttoolsTopicName, 'ChartPlotting/SCP_chart_plotting.html', chartingTopicNode)
    allNodes.add(charttoolsTopicNode)

    for webpageNode in allNodes:
        sideBarStr = '</head>\n<body>\n\n<div class="sidenav">\n'+ MFPWebSiteNode.outputSideBar(webpageNode, lang) + '</div>\n\n<div class="main">\n'

        titleStr = ''
        bodyStrStart = False
        bodyStr = ''
        with open(sourceWebPagesFolder + '/' + lang + '/' + webpageNode.pageFilePath, 'r', encoding="utf-8") as f:
            for line in f:
                lineNoBlank = line.lstrip().lower()
                # For each line, check if line contains the string
                if lineNoBlank.startswith('<title>') and ('</title>' in lineNoBlank):
                    titleStr = line
                if (not bodyStrStart) and lineNoBlank.startswith('<body style="background-color:white;">'):
                    bodyStrStart = True
                elif bodyStrStart:
                    if lineNoBlank.startswith('</body>'):
                        bodyStrStart = False
                    else:
                        bodyStr += line
                
        fullTextStr = styleStr + titleStr + sideBarStr.replace('<a href="', '<a href="' + webpageNode.upperLevelStr) + bodyStr + endOfFileStr
        with open(destWebPagesFolder + '/' + lang + '/' + webpageNode.pageFilePath, 'w', encoding="utf-8") as f:
            f.write(fullTextStr)
            
            

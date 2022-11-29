from src.reseau.types.AbstractPlayerSearchInformation import AbstractPlayerSearchInformation
from src.reseau.types.AccountTagInformation import AccountTagInformation
from src.reseau.types.PlayerSearchCharacterNameInformation import PlayerSearchCharacterNameInformation
from src.reseau.types.PlayerSearchTagInformation import PlayerSearchTagInformation
from src.reseau.types.StatisticData import StatisticData
from src.reseau.types.StatisticDataBoolean import StatisticDataBoolean
from src.reseau.types.StatisticDataByte import StatisticDataByte
from src.reseau.types.StatisticDataInt import StatisticDataInt
from src.reseau.types.StatisticDataShort import StatisticDataShort
from src.reseau.types.StatisticDataString import StatisticDataString
from src.reseau.types.GameServerInformations import GameServerInformations
from src.reseau.types.Achievement import Achievement
from src.reseau.types.AchievementAchieved import AchievementAchieved
from src.reseau.types.AchievementAchievedRewardable import AchievementAchievedRewardable
from src.reseau.types.AchievementObjective import AchievementObjective
from src.reseau.types.AchievementStartedObjective import AchievementStartedObjective
from src.reseau.types.FightDispellableEffectExtendedInformations import FightDispellableEffectExtendedInformations
from src.reseau.types.AbstractFightDispellableEffect import AbstractFightDispellableEffect
from src.reseau.types.FightTemporaryBoostEffect import FightTemporaryBoostEffect
from src.reseau.types.FightTemporaryBoostStateEffect import FightTemporaryBoostStateEffect
from src.reseau.types.FightTemporaryBoostWeaponDamagesEffect import FightTemporaryBoostWeaponDamagesEffect
from src.reseau.types.FightTemporarySpellBoostEffect import FightTemporarySpellBoostEffect
from src.reseau.types.FightTemporarySpellImmunityEffect import FightTemporarySpellImmunityEffect
from src.reseau.types.FightTriggeredEffect import FightTriggeredEffect
from src.reseau.types.GameActionMark import GameActionMark
from src.reseau.types.GameActionMarkedCell import GameActionMarkedCell
from src.reseau.types.ServerSessionConstant import ServerSessionConstant
from src.reseau.types.ServerSessionConstantInteger import ServerSessionConstantInteger
from src.reseau.types.ServerSessionConstantLong import ServerSessionConstantLong
from src.reseau.types.ServerSessionConstantString import ServerSessionConstantString
from src.reseau.types.AbstractCharacterInformation import AbstractCharacterInformation
from src.reseau.types.CharacterBasicMinimalInformations import CharacterBasicMinimalInformations
from src.reseau.types.CharacterMinimalAllianceInformations import CharacterMinimalAllianceInformations
from src.reseau.types.CharacterMinimalGuildInformations import CharacterMinimalGuildInformations
from src.reseau.types.CharacterMinimalGuildPublicInformations import CharacterMinimalGuildPublicInformations
from src.reseau.types.CharacterMinimalInformations import CharacterMinimalInformations
from src.reseau.types.CharacterMinimalPlusLookAndGradeInformations import CharacterMinimalPlusLookAndGradeInformations
from src.reseau.types.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations
from src.reseau.types.ActorAlignmentInformations import ActorAlignmentInformations
from src.reseau.types.ActorExtendedAlignmentInformations import ActorExtendedAlignmentInformations
from src.reseau.types.AlterationInfo import AlterationInfo
from src.reseau.types.CharacterCharacteristic import CharacterCharacteristic
from src.reseau.types.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed
from src.reseau.types.CharacterCharacteristics import CharacterCharacteristics
from src.reseau.types.CharacterCharacteristicsInformations import CharacterCharacteristicsInformations
from src.reseau.types.CharacterCharacteristicValue import CharacterCharacteristicValue
from src.reseau.types.CharacterSpellModification import CharacterSpellModification
from src.reseau.types.CharacterUsableCharacteristicDetailed import CharacterUsableCharacteristicDetailed
from src.reseau.types.CharacterBaseInformations import CharacterBaseInformations
from src.reseau.types.CharacterHardcoreOrEpicInformations import CharacterHardcoreOrEpicInformations
from src.reseau.types.CharacterRemodelingInformation import CharacterRemodelingInformation
from src.reseau.types.CharacterToRemodelInformations import CharacterToRemodelInformations
from src.reseau.types.RemodelingInformation import RemodelingInformation
from src.reseau.types.DebtInformation import DebtInformation
from src.reseau.types.KamaDebtInformation import KamaDebtInformation
from src.reseau.types.PlayerNote import PlayerNote
from src.reseau.types.ActorRestrictionsInformations import ActorRestrictionsInformations
from src.reseau.types.PlayerStatus import PlayerStatus
from src.reseau.types.PlayerStatusExtended import PlayerStatusExtended
from src.reseau.types.ActorOrientation import ActorOrientation
from src.reseau.types.EntityDispositionInformations import EntityDispositionInformations
from src.reseau.types.EntityMovementInformations import EntityMovementInformations
from src.reseau.types.FightEntityDispositionInformations import FightEntityDispositionInformations
from src.reseau.types.GameContextActorInformations import GameContextActorInformations
from src.reseau.types.GameContextActorPositionInformations import GameContextActorPositionInformations
from src.reseau.types.GameRolePlayTaxCollectorInformations import GameRolePlayTaxCollectorInformations
from src.reseau.types.IdentifiedEntityDispositionInformations import IdentifiedEntityDispositionInformations
from src.reseau.types.MapCoordinates import MapCoordinates
from src.reseau.types.MapCoordinatesAndId import MapCoordinatesAndId
from src.reseau.types.MapCoordinatesExtended import MapCoordinatesExtended
from src.reseau.types.TaxCollectorStaticExtendedInformations import TaxCollectorStaticExtendedInformations
from src.reseau.types.TaxCollectorStaticInformations import TaxCollectorStaticInformations
from src.reseau.types.AbstractFightTeamInformations import AbstractFightTeamInformations
from src.reseau.types.BaseSpawnMonsterInformation import BaseSpawnMonsterInformation
from src.reseau.types.FightAllianceTeamInformations import FightAllianceTeamInformations
from src.reseau.types.FightCommonInformations import FightCommonInformations
from src.reseau.types.FightExternalInformations import FightExternalInformations
from src.reseau.types.FightLoot import FightLoot
from src.reseau.types.FightLootObject import FightLootObject
from src.reseau.types.FightOptionsInformations import FightOptionsInformations
from src.reseau.types.FightResultAdditionalData import FightResultAdditionalData
from src.reseau.types.FightResultExperienceData import FightResultExperienceData
from src.reseau.types.FightResultFighterListEntry import FightResultFighterListEntry
from src.reseau.types.FightResultListEntry import FightResultListEntry
from src.reseau.types.FightResultMutantListEntry import FightResultMutantListEntry
from src.reseau.types.FightResultPlayerListEntry import FightResultPlayerListEntry
from src.reseau.types.FightResultPvpData import FightResultPvpData
from src.reseau.types.FightResultTaxCollectorListEntry import FightResultTaxCollectorListEntry
from src.reseau.types.FightStartingPositions import FightStartingPositions
from src.reseau.types.FightTeamInformations import FightTeamInformations
from src.reseau.types.FightTeamLightInformations import FightTeamLightInformations
from src.reseau.types.FightTeamMemberCharacterInformations import FightTeamMemberCharacterInformations
from src.reseau.types.FightTeamMemberEntityInformation import FightTeamMemberEntityInformation
from src.reseau.types.FightTeamMemberInformations import FightTeamMemberInformations
from src.reseau.types.FightTeamMemberMonsterInformations import FightTeamMemberMonsterInformations
from src.reseau.types.FightTeamMemberTaxCollectorInformations import FightTeamMemberTaxCollectorInformations
from src.reseau.types.FightTeamMemberWithAllianceCharacterInformations import FightTeamMemberWithAllianceCharacterInformations
from src.reseau.types.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
from src.reseau.types.GameContextSummonsInformation import GameContextSummonsInformation
from src.reseau.types.GameFightAIInformations import GameFightAIInformations
from src.reseau.types.GameFightCharacterInformations import GameFightCharacterInformations
from src.reseau.types.GameFightCharacteristics import GameFightCharacteristics
from src.reseau.types.GameFightEffectTriggerCount import GameFightEffectTriggerCount
from src.reseau.types.GameFightEntityInformation import GameFightEntityInformation
from src.reseau.types.GameFightFighterEntityLightInformation import GameFightFighterEntityLightInformation
from src.reseau.types.GameFightFighterInformations import GameFightFighterInformations
from src.reseau.types.GameFightFighterLightInformations import GameFightFighterLightInformations
from src.reseau.types.GameFightFighterMonsterLightInformations import GameFightFighterMonsterLightInformations
from src.reseau.types.GameFightFighterNamedInformations import GameFightFighterNamedInformations
from src.reseau.types.GameFightFighterNamedLightInformations import GameFightFighterNamedLightInformations
from src.reseau.types.GameFightFighterTaxCollectorLightInformations import GameFightFighterTaxCollectorLightInformations
from src.reseau.types.GameFightMonsterInformations import GameFightMonsterInformations
from src.reseau.types.GameFightMonsterWithAlignmentInformations import GameFightMonsterWithAlignmentInformations
from src.reseau.types.GameFightMutantInformations import GameFightMutantInformations
from src.reseau.types.GameFightResumeSlaveInfo import GameFightResumeSlaveInfo
from src.reseau.types.GameFightSpellCooldown import GameFightSpellCooldown
from src.reseau.types.GameFightTaxCollectorInformations import GameFightTaxCollectorInformations
from src.reseau.types.SpawnCharacterInformation import SpawnCharacterInformation
from src.reseau.types.SpawnCompanionInformation import SpawnCompanionInformation
from src.reseau.types.SpawnInformation import SpawnInformation
from src.reseau.types.SpawnMonsterInformation import SpawnMonsterInformation
from src.reseau.types.SpawnScaledMonsterInformation import SpawnScaledMonsterInformation
from src.reseau.types.AllianceInformations import AllianceInformations
from src.reseau.types.AlternativeMonstersInGroupLightInformations import AlternativeMonstersInGroupLightInformations
from src.reseau.types.AnomalySubareaInformation import AnomalySubareaInformation
from src.reseau.types.AtlasPointsInformations import AtlasPointsInformations
from src.reseau.types.BasicAllianceInformations import BasicAllianceInformations
from src.reseau.types.BasicGuildInformations import BasicGuildInformations
from src.reseau.types.BasicNamedAllianceInformations import BasicNamedAllianceInformations
from src.reseau.types.GameRolePlayActorInformations import GameRolePlayActorInformations
from src.reseau.types.GameRolePlayCharacterInformations import GameRolePlayCharacterInformations
from src.reseau.types.GameRolePlayGroupMonsterInformations import GameRolePlayGroupMonsterInformations
from src.reseau.types.GameRolePlayGroupMonsterWaveInformations import GameRolePlayGroupMonsterWaveInformations
from src.reseau.types.GameRolePlayHumanoidInformations import GameRolePlayHumanoidInformations
from src.reseau.types.GameRolePlayMerchantInformations import GameRolePlayMerchantInformations
from src.reseau.types.GameRolePlayMountInformations import GameRolePlayMountInformations
from src.reseau.types.GameRolePlayMutantInformations import GameRolePlayMutantInformations
from src.reseau.types.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations
from src.reseau.types.GameRolePlayNpcInformations import GameRolePlayNpcInformations
from src.reseau.types.GameRolePlayNpcWithQuestInformations import GameRolePlayNpcWithQuestInformations
from src.reseau.types.GameRolePlayPortalInformations import GameRolePlayPortalInformations
from src.reseau.types.GameRolePlayPrismInformations import GameRolePlayPrismInformations
from src.reseau.types.GameRolePlayTreasureHintInformations import GameRolePlayTreasureHintInformations
from src.reseau.types.GroupMonsterStaticInformations import GroupMonsterStaticInformations
from src.reseau.types.GroupMonsterStaticInformationsWithAlternatives import GroupMonsterStaticInformationsWithAlternatives
from src.reseau.types.GuildInAllianceInformations import GuildInAllianceInformations
from src.reseau.types.GuildInformations import GuildInformations
from src.reseau.types.HumanInformations import HumanInformations
from src.reseau.types.HumanOption import HumanOption
from src.reseau.types.HumanOptionAlliance import HumanOptionAlliance
from src.reseau.types.HumanOptionEmote import HumanOptionEmote
from src.reseau.types.HumanOptionFollowers import HumanOptionFollowers
from src.reseau.types.HumanOptionGuild import HumanOptionGuild
from src.reseau.types.HumanOptionObjectUse import HumanOptionObjectUse
from src.reseau.types.HumanOptionOrnament import HumanOptionOrnament
from src.reseau.types.HumanOptionSkillUse import HumanOptionSkillUse
from src.reseau.types.HumanOptionSpeedMultiplier import HumanOptionSpeedMultiplier
from src.reseau.types.HumanOptionTitle import HumanOptionTitle
from src.reseau.types.MonsterBoosts import MonsterBoosts
from src.reseau.types.MonsterInGroupInformations import MonsterInGroupInformations
from src.reseau.types.MonsterInGroupLightInformations import MonsterInGroupLightInformations
from src.reseau.types.ObjectItemInRolePlay import ObjectItemInRolePlay
from src.reseau.types.AlignmentWarEffortInformation import AlignmentWarEffortInformation
from src.reseau.types.BreachBranch import BreachBranch
from src.reseau.types.BreachReward import BreachReward
from src.reseau.types.ExtendedBreachBranch import ExtendedBreachBranch
from src.reseau.types.ExtendedLockedBreachBranch import ExtendedLockedBreachBranch
from src.reseau.types.ArenaLeagueRanking import ArenaLeagueRanking
from src.reseau.types.ArenaRankInfos import ArenaRankInfos
from src.reseau.types.ArenaRanking import ArenaRanking
from src.reseau.types.LeagueFriendInformations import LeagueFriendInformations
from src.reseau.types.DecraftedItemStackInfo import DecraftedItemStackInfo
from src.reseau.types.JobBookSubscription import JobBookSubscription
from src.reseau.types.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo
from src.reseau.types.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
from src.reseau.types.JobCrafterDirectoryListEntry import JobCrafterDirectoryListEntry
from src.reseau.types.JobCrafterDirectorySettings import JobCrafterDirectorySettings
from src.reseau.types.JobDescription import JobDescription
from src.reseau.types.JobExperience import JobExperience
from src.reseau.types.MapNpcQuestInfo import MapNpcQuestInfo
from src.reseau.types.DungeonPartyFinderPlayer import DungeonPartyFinderPlayer
from src.reseau.types.NamedPartyTeam import NamedPartyTeam
from src.reseau.types.NamedPartyTeamWithOutcome import NamedPartyTeamWithOutcome
from src.reseau.types.PartyGuestInformations import PartyGuestInformations
from src.reseau.types.PartyInvitationMemberInformations import PartyInvitationMemberInformations
from src.reseau.types.PartyMemberArenaInformations import PartyMemberArenaInformations
from src.reseau.types.PartyMemberGeoPosition import PartyMemberGeoPosition
from src.reseau.types.PartyMemberInformations import PartyMemberInformations
from src.reseau.types.PartyEntityBaseInformation import PartyEntityBaseInformation
from src.reseau.types.PartyEntityMemberInformation import PartyEntityMemberInformation
from src.reseau.types.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag
from src.reseau.types.QuestActiveDetailedInformations import QuestActiveDetailedInformations
from src.reseau.types.QuestActiveInformations import QuestActiveInformations
from src.reseau.types.QuestObjectiveInformations import QuestObjectiveInformations
from src.reseau.types.QuestObjectiveInformationsWithCompletion import QuestObjectiveInformationsWithCompletion
from src.reseau.types.PortalInformation import PortalInformation
from src.reseau.types.TreasureHuntFlag import TreasureHuntFlag
from src.reseau.types.TreasureHuntStep import TreasureHuntStep
from src.reseau.types.TreasureHuntStepDig import TreasureHuntStepDig
from src.reseau.types.TreasureHuntStepFight import TreasureHuntStepFight
from src.reseau.types.TreasureHuntStepFollowDirection import TreasureHuntStepFollowDirection
from src.reseau.types.TreasureHuntStepFollowDirectionToHint import TreasureHuntStepFollowDirectionToHint
from src.reseau.types.TreasureHuntStepFollowDirectionToPOI import TreasureHuntStepFollowDirectionToPOI
from src.reseau.types.BidExchangerObjectInfo import BidExchangerObjectInfo
from src.reseau.types.ForgettableSpellItem import ForgettableSpellItem
from src.reseau.types.GoldItem import GoldItem
from src.reseau.types.Item import Item
from src.reseau.types.ObjectEffects import ObjectEffects
from src.reseau.types.ObjectItem import ObjectItem
from src.reseau.types.ObjectItemGenericQuantity import ObjectItemGenericQuantity
from src.reseau.types.ObjectItemInformationWithQuantity import ObjectItemInformationWithQuantity
from src.reseau.types.ObjectItemMinimalInformation import ObjectItemMinimalInformation
from src.reseau.types.ObjectItemNotInContainer import ObjectItemNotInContainer
from src.reseau.types.ObjectItemQuantity import ObjectItemQuantity
from src.reseau.types.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects
from src.reseau.types.ObjectItemToSell import ObjectItemToSell
from src.reseau.types.ObjectItemToSellInBid import ObjectItemToSellInBid
from src.reseau.types.ObjectItemToSellInHumanVendorShop import ObjectItemToSellInHumanVendorShop
from src.reseau.types.ObjectItemToSellInNpcShop import ObjectItemToSellInNpcShop
from src.reseau.types.SellerBuyerDescriptor import SellerBuyerDescriptor
from src.reseau.types.SpellItem import SpellItem
from src.reseau.types.ObjectEffect import ObjectEffect
from src.reseau.types.ObjectEffectCreature import ObjectEffectCreature
from src.reseau.types.ObjectEffectDate import ObjectEffectDate
from src.reseau.types.ObjectEffectDice import ObjectEffectDice
from src.reseau.types.ObjectEffectDuration import ObjectEffectDuration
from src.reseau.types.ObjectEffectInteger import ObjectEffectInteger
from src.reseau.types.ObjectEffectLadder import ObjectEffectLadder
from src.reseau.types.ObjectEffectMinMax import ObjectEffectMinMax
from src.reseau.types.ObjectEffectMount import ObjectEffectMount
from src.reseau.types.ObjectEffectString import ObjectEffectString
from src.reseau.types.EntityInformation import EntityInformation
from src.reseau.types.ProtectedEntityWaitingForHelpInfo import ProtectedEntityWaitingForHelpInfo
from src.reseau.types.FinishMoveInformations import FinishMoveInformations
from src.reseau.types.AbstractContactInformations import AbstractContactInformations
from src.reseau.types.AcquaintanceInformation import AcquaintanceInformation
from src.reseau.types.AcquaintanceOnlineInformation import AcquaintanceOnlineInformation
from src.reseau.types.FriendInformations import FriendInformations
from src.reseau.types.FriendOnlineInformations import FriendOnlineInformations
from src.reseau.types.FriendSpouseInformations import FriendSpouseInformations
from src.reseau.types.FriendSpouseOnlineInformations import FriendSpouseOnlineInformations
from src.reseau.types.IgnoredInformations import IgnoredInformations
from src.reseau.types.IgnoredOnlineInformations import IgnoredOnlineInformations
from src.reseau.types.Contribution import Contribution
from src.reseau.types.GuildEmblem import GuildEmblem
from src.reseau.types.GuildMember import GuildMember
from src.reseau.types.GuildRankInformation import GuildRankInformation
from src.reseau.types.GuildRankMinimalInformation import GuildRankMinimalInformation
from src.reseau.types.GuildRankPublicInformation import GuildRankPublicInformation
from src.reseau.types.HavenBagFurnitureInformation import HavenBagFurnitureInformation
from src.reseau.types.ApplicationPlayerInformation import ApplicationPlayerInformation
from src.reseau.types.GuildApplicationInformation import GuildApplicationInformation
from src.reseau.types.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
from src.reseau.types.GuildLogbookChestActivity import GuildLogbookChestActivity
from src.reseau.types.GuildLevelUpActivity import GuildLevelUpActivity
from src.reseau.types.GuildPaddockActivity import GuildPaddockActivity
from src.reseau.types.GuildPlayerFlowActivity import GuildPlayerFlowActivity
from src.reseau.types.GuildPlayerRankUpdateActivity import GuildPlayerRankUpdateActivity
from src.reseau.types.GuildRankActivity import GuildRankActivity
from src.reseau.types.GuildUnlockNewTabActivity import GuildUnlockNewTabActivity
from src.reseau.types.GuildRecruitmentInformation import GuildRecruitmentInformation
from src.reseau.types.AdditionalTaxCollectorInformations import AdditionalTaxCollectorInformations
from src.reseau.types.TaxCollectorBasicInformations import TaxCollectorBasicInformations
from src.reseau.types.TaxCollectorComplementaryInformations import TaxCollectorComplementaryInformations
from src.reseau.types.TaxCollectorFightersInformation import TaxCollectorFightersInformation
from src.reseau.types.TaxCollectorGuildInformations import TaxCollectorGuildInformations
from src.reseau.types.TaxCollectorInformations import TaxCollectorInformations
from src.reseau.types.TaxCollectorLootInformations import TaxCollectorLootInformations
from src.reseau.types.TaxCollectorMovement import TaxCollectorMovement
from src.reseau.types.TaxCollectorWaitingForHelpInformations import TaxCollectorWaitingForHelpInformations
from src.reseau.types.HavenBagRoomPreviewInformation import HavenBagRoomPreviewInformation
from src.reseau.types.AccountHouseInformations import AccountHouseInformations
from src.reseau.types.HouseGuildedInformations import HouseGuildedInformations
from src.reseau.types.HouseInformations import HouseInformations
from src.reseau.types.HouseInformationsForGuild import HouseInformationsForGuild
from src.reseau.types.HouseInformationsForSell import HouseInformationsForSell
from src.reseau.types.HouseInformationsInside import HouseInformationsInside
from src.reseau.types.HouseInstanceInformations import HouseInstanceInformations
from src.reseau.types.HouseOnMapInformations import HouseOnMapInformations
from src.reseau.types.Idol import Idol
from src.reseau.types.PartyIdol import PartyIdol
from src.reseau.types.InteractiveElement import InteractiveElement
from src.reseau.types.InteractiveElementNamedSkill import InteractiveElementNamedSkill
from src.reseau.types.InteractiveElementSkill import InteractiveElementSkill
from src.reseau.types.InteractiveElementWithAgeBonus import InteractiveElementWithAgeBonus
from src.reseau.types.MapObstacle import MapObstacle
from src.reseau.types.StatedElement import StatedElement
from src.reseau.types.SkillActionDescription import SkillActionDescription
from src.reseau.types.SkillActionDescriptionCollect import SkillActionDescriptionCollect
from src.reseau.types.SkillActionDescriptionCraft import SkillActionDescriptionCraft
from src.reseau.types.SkillActionDescriptionTimed import SkillActionDescriptionTimed
from src.reseau.types.TeleportDestination import TeleportDestination
from src.reseau.types.StorageTabInformation import StorageTabInformation
from src.reseau.types.UpdatedStorageTabInformation import UpdatedStorageTabInformation
from src.reseau.types.RecycledItem import RecycledItem
from src.reseau.types.EntityLook import EntityLook
from src.reseau.types.IndexedEntityLook import IndexedEntityLook
from src.reseau.types.SubEntity import SubEntity
from src.reseau.types.ItemDurability import ItemDurability
from src.reseau.types.MountClientData import MountClientData
from src.reseau.types.UpdateMountBooleanCharacteristic import UpdateMountBooleanCharacteristic
from src.reseau.types.UpdateMountCharacteristic import UpdateMountCharacteristic
from src.reseau.types.UpdateMountIntegerCharacteristic import UpdateMountIntegerCharacteristic
from src.reseau.types.MountInformationsForPaddock import MountInformationsForPaddock
from src.reseau.types.PaddockBuyableInformations import PaddockBuyableInformations
from src.reseau.types.PaddockContentInformations import PaddockContentInformations
from src.reseau.types.PaddockGuildedInformations import PaddockGuildedInformations
from src.reseau.types.PaddockInformations import PaddockInformations
from src.reseau.types.PaddockInformationsForSell import PaddockInformationsForSell
from src.reseau.types.PaddockInstancesInformations import PaddockInstancesInformations
from src.reseau.types.PaddockItem import PaddockItem
from src.reseau.types.CharacterCharacteristicForPreset import CharacterCharacteristicForPreset
from src.reseau.types.EntitiesPreset import EntitiesPreset
from src.reseau.types.ForgettableSpellsPreset import ForgettableSpellsPreset
from src.reseau.types.FullStatsPreset import FullStatsPreset
from src.reseau.types.IconNamedPreset import IconNamedPreset
from src.reseau.types.IdolsPreset import IdolsPreset
from src.reseau.types.ItemForPreset import ItemForPreset
from src.reseau.types.ItemsPreset import ItemsPreset
from src.reseau.types.Preset import Preset
from src.reseau.types.PresetsContainerPreset import PresetsContainerPreset
from src.reseau.types.SimpleCharacterCharacteristicForPreset import SimpleCharacterCharacteristicForPreset
from src.reseau.types.SpellForPreset import SpellForPreset
from src.reseau.types.SpellsPreset import SpellsPreset
from src.reseau.types.StatsPreset import StatsPreset
from src.reseau.types.AllianceInsiderPrismInformation import AllianceInsiderPrismInformation
from src.reseau.types.AlliancePrismInformation import AlliancePrismInformation
from src.reseau.types.PrismFightersInformation import PrismFightersInformation
from src.reseau.types.PrismGeolocalizedInformation import PrismGeolocalizedInformation
from src.reseau.types.PrismInformation import PrismInformation
from src.reseau.types.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo
from src.reseau.types.Shortcut import Shortcut
from src.reseau.types.ShortcutEmote import ShortcutEmote
from src.reseau.types.ShortcutEntitiesPreset import ShortcutEntitiesPreset
from src.reseau.types.ShortcutObject import ShortcutObject
from src.reseau.types.ShortcutObjectIdolsPreset import ShortcutObjectIdolsPreset
from src.reseau.types.ShortcutObjectItem import ShortcutObjectItem
from src.reseau.types.ShortcutObjectPreset import ShortcutObjectPreset
from src.reseau.types.ShortcutSmiley import ShortcutSmiley
from src.reseau.types.ShortcutSpell import ShortcutSpell
from src.reseau.types.AbstractSocialGroupInfos import AbstractSocialGroupInfos
from src.reseau.types.AlliancedGuildFactSheetInformations import AlliancedGuildFactSheetInformations
from src.reseau.types.AllianceFactSheetInformations import AllianceFactSheetInformations
from src.reseau.types.GuildFactSheetInformations import GuildFactSheetInformations
from src.reseau.types.GuildInAllianceVersatileInformations import GuildInAllianceVersatileInformations
from src.reseau.types.GuildInsiderFactSheetInformations import GuildInsiderFactSheetInformations
from src.reseau.types.GuildVersatileInformations import GuildVersatileInformations
from src.reseau.types.StartupActionAddObject import StartupActionAddObject
from src.reseau.types.TrustCertificate import TrustCertificate
from src.reseau.types.Version import Version
from src.reseau.types.BufferInformation import BufferInformation
class TypesFactory:
    id_class = {
    "404": AbstractPlayerSearchInformation,
    "28": AccountTagInformation,
    "5825": PlayerSearchCharacterNameInformation,
    "9765": PlayerSearchTagInformation,
    "724": StatisticData,
    "7915": StatisticDataBoolean,
    "6322": StatisticDataByte,
    "6013": StatisticDataInt,
    "2628": StatisticDataShort,
    "2932": StatisticDataString,
    "5079": GameServerInformations,
    "1179": Achievement,
    "3382": AchievementAchieved,
    "710": AchievementAchievedRewardable,
    "7005": AchievementObjective,
    "3632": AchievementStartedObjective,
    "9388": FightDispellableEffectExtendedInformations,
    "8111": AbstractFightDispellableEffect,
    "3948": FightTemporaryBoostEffect,
    "1065": FightTemporaryBoostStateEffect,
    "8193": FightTemporaryBoostWeaponDamagesEffect,
    "9316": FightTemporarySpellBoostEffect,
    "1263": FightTemporarySpellImmunityEffect,
    "7980": FightTriggeredEffect,
    "5611": GameActionMark,
    "4086": GameActionMarkedCell,
    "1785": ServerSessionConstant,
    "4636": ServerSessionConstantInteger,
    "4766": ServerSessionConstantLong,
    "2699": ServerSessionConstantString,
    "5595": AbstractCharacterInformation,
    "2071": CharacterBasicMinimalInformations,
    "114": CharacterMinimalAllianceInformations,
    "4459": CharacterMinimalGuildInformations,
    "9962": CharacterMinimalGuildPublicInformations,
    "2090": CharacterMinimalInformations,
    "8828": CharacterMinimalPlusLookAndGradeInformations,
    "9849": CharacterMinimalPlusLookInformations,
    "3113": ActorAlignmentInformations,
    "4619": ActorExtendedAlignmentInformations,
    "7488": AlterationInfo,
    "2806": CharacterCharacteristic,
    "8713": CharacterCharacteristicDetailed,
    "9673": CharacterCharacteristics,
    "8082": CharacterCharacteristicsInformations,
    "4266": CharacterCharacteristicValue,
    "5279": CharacterSpellModification,
    "4393": CharacterUsableCharacteristicDetailed,
    "3420": CharacterBaseInformations,
    "9676": CharacterHardcoreOrEpicInformations,
    "9075": CharacterRemodelingInformation,
    "4175": CharacterToRemodelInformations,
    "14": RemodelingInformation,
    "1480": DebtInformation,
    "1081": KamaDebtInformation,
    "5139": PlayerNote,
    "7613": ActorRestrictionsInformations,
    "8044": PlayerStatus,
    "2436": PlayerStatusExtended,
    "3934": ActorOrientation,
    "5526": EntityDispositionInformations,
    "7524": EntityMovementInformations,
    "5058": FightEntityDispositionInformations,
    "9721": GameContextActorInformations,
    "4458": GameContextActorPositionInformations,
    "9431": GameRolePlayTaxCollectorInformations,
    "3649": IdentifiedEntityDispositionInformations,
    "6365": MapCoordinates,
    "7072": MapCoordinatesAndId,
    "3068": MapCoordinatesExtended,
    "4323": TaxCollectorStaticExtendedInformations,
    "723": TaxCollectorStaticInformations,
    "7127": AbstractFightTeamInformations,
    "7394": BaseSpawnMonsterInformation,
    "9213": FightAllianceTeamInformations,
    "5521": FightCommonInformations,
    "9404": FightExternalInformations,
    "2813": FightLoot,
    "6053": FightLootObject,
    "9809": FightOptionsInformations,
    "4221": FightResultAdditionalData,
    "4058": FightResultExperienceData,
    "8625": FightResultFighterListEntry,
    "2945": FightResultListEntry,
    "8609": FightResultMutantListEntry,
    "6469": FightResultPlayerListEntry,
    "8005": FightResultPvpData,
    "7213": FightResultTaxCollectorListEntry,
    "7912": FightStartingPositions,
    "2808": FightTeamInformations,
    "4394": FightTeamLightInformations,
    "8121": FightTeamMemberCharacterInformations,
    "1608": FightTeamMemberEntityInformation,
    "5904": FightTeamMemberInformations,
    "3893": FightTeamMemberMonsterInformations,
    "7905": FightTeamMemberTaxCollectorInformations,
    "5359": FightTeamMemberWithAllianceCharacterInformations,
    "5907": GameContextBasicSpawnInformation,
    "5292": GameContextSummonsInformation,
    "970": GameFightAIInformations,
    "27": GameFightCharacterInformations,
    "7440": GameFightCharacteristics,
    "9278": GameFightEffectTriggerCount,
    "4167": GameFightEntityInformation,
    "3441": GameFightFighterEntityLightInformation,
    "7438": GameFightFighterInformations,
    "9211": GameFightFighterLightInformations,
    "1602": GameFightFighterMonsterLightInformations,
    "3344": GameFightFighterNamedInformations,
    "2171": GameFightFighterNamedLightInformations,
    "4004": GameFightFighterTaxCollectorLightInformations,
    "8909": GameFightMonsterInformations,
    "9978": GameFightMonsterWithAlignmentInformations,
    "1454": GameFightMutantInformations,
    "693": GameFightResumeSlaveInfo,
    "8381": GameFightSpellCooldown,
    "2540": GameFightTaxCollectorInformations,
    "8521": SpawnCharacterInformation,
    "3358": SpawnCompanionInformation,
    "1821": SpawnInformation,
    "7219": SpawnMonsterInformation,
    "7315": SpawnScaledMonsterInformation,
    "8147": AllianceInformations,
    "2119": AlternativeMonstersInGroupLightInformations,
    "7135": AnomalySubareaInformation,
    "7189": AtlasPointsInformations,
    "7034": BasicAllianceInformations,
    "4121": BasicGuildInformations,
    "4381": BasicNamedAllianceInformations,
    "2936": GameRolePlayActorInformations,
    "9847": GameRolePlayCharacterInformations,
    "5562": GameRolePlayGroupMonsterInformations,
    "3133": GameRolePlayGroupMonsterWaveInformations,
    "3654": GameRolePlayHumanoidInformations,
    "2148": GameRolePlayMerchantInformations,
    "6935": GameRolePlayMountInformations,
    "2472": GameRolePlayMutantInformations,
    "4711": GameRolePlayNamedActorInformations,
    "3198": GameRolePlayNpcInformations,
    "7460": GameRolePlayNpcWithQuestInformations,
    "5287": GameRolePlayPortalInformations,
    "8903": GameRolePlayPrismInformations,
    "8341": GameRolePlayTreasureHintInformations,
    "7245": GroupMonsterStaticInformations,
    "8822": GroupMonsterStaticInformationsWithAlternatives,
    "2857": GuildInAllianceInformations,
    "4294": GuildInformations,
    "5754": HumanInformations,
    "3744": HumanOption,
    "4551": HumanOptionAlliance,
    "544": HumanOptionEmote,
    "9551": HumanOptionFollowers,
    "4624": HumanOptionGuild,
    "3502": HumanOptionObjectUse,
    "4240": HumanOptionOrnament,
    "9785": HumanOptionSkillUse,
    "2528": HumanOptionSpeedMultiplier,
    "153": HumanOptionTitle,
    "7310": MonsterBoosts,
    "7097": MonsterInGroupInformations,
    "8529": MonsterInGroupLightInformations,
    "3401": ObjectItemInRolePlay,
    "2271": AlignmentWarEffortInformation,
    "5819": BreachBranch,
    "5994": BreachReward,
    "8013": ExtendedBreachBranch,
    "9732": ExtendedLockedBreachBranch,
    "5760": ArenaLeagueRanking,
    "9310": ArenaRankInfos,
    "5011": ArenaRanking,
    "5881": LeagueFriendInformations,
    "6977": DecraftedItemStackInfo,
    "3527": JobBookSubscription,
    "8145": JobCrafterDirectoryEntryJobInfo,
    "3092": JobCrafterDirectoryEntryPlayerInfo,
    "7933": JobCrafterDirectoryListEntry,
    "496": JobCrafterDirectorySettings,
    "4722": JobDescription,
    "8421": JobExperience,
    "8240": MapNpcQuestInfo,
    "6327": DungeonPartyFinderPlayer,
    "5067": NamedPartyTeam,
    "3954": NamedPartyTeamWithOutcome,
    "3703": PartyGuestInformations,
    "5868": PartyInvitationMemberInformations,
    "4555": PartyMemberArenaInformations,
    "7996": PartyMemberGeoPosition,
    "7227": PartyMemberInformations,
    "6690": PartyEntityBaseInformation,
    "3304": PartyEntityMemberInformation,
    "8611": GameRolePlayNpcQuestFlag,
    "4047": QuestActiveDetailedInformations,
    "8162": QuestActiveInformations,
    "1278": QuestObjectiveInformations,
    "4698": QuestObjectiveInformationsWithCompletion,
    "4591": PortalInformation,
    "7446": TreasureHuntFlag,
    "9260": TreasureHuntStep,
    "7366": TreasureHuntStepDig,
    "9094": TreasureHuntStepFight,
    "4354": TreasureHuntStepFollowDirection,
    "3582": TreasureHuntStepFollowDirectionToHint,
    "8072": TreasureHuntStepFollowDirectionToPOI,
    "3368": BidExchangerObjectInfo,
    "1213": ForgettableSpellItem,
    "3223": GoldItem,
    "7430": Item,
    "8945": ObjectEffects,
    "4173": ObjectItem,
    "8490": ObjectItemGenericQuantity,
    "8372": ObjectItemInformationWithQuantity,
    "3831": ObjectItemMinimalInformation,
    "9890": ObjectItemNotInContainer,
    "9835": ObjectItemQuantity,
    "8614": ObjectItemQuantityPriceDateEffects,
    "2962": ObjectItemToSell,
    "7565": ObjectItemToSellInBid,
    "8539": ObjectItemToSellInHumanVendorShop,
    "9244": ObjectItemToSellInNpcShop,
    "7687": SellerBuyerDescriptor,
    "4007": SpellItem,
    "15": ObjectEffect,
    "8531": ObjectEffectCreature,
    "4507": ObjectEffectDate,
    "5043": ObjectEffectDice,
    "5384": ObjectEffectDuration,
    "184": ObjectEffectInteger,
    "6069": ObjectEffectLadder,
    "3274": ObjectEffectMinMax,
    "5795": ObjectEffectMount,
    "238": ObjectEffectString,
    "1022": EntityInformation,
    "2923": ProtectedEntityWaitingForHelpInfo,
    "8323": FinishMoveInformations,
    "1975": AbstractContactInformations,
    "2995": AcquaintanceInformation,
    "6325": AcquaintanceOnlineInformation,
    "7257": FriendInformations,
    "7420": FriendOnlineInformations,
    "9604": FriendSpouseInformations,
    "3993": FriendSpouseOnlineInformations,
    "9408": IgnoredInformations,
    "5031": IgnoredOnlineInformations,
    "1328": Contribution,
    "1272": GuildEmblem,
    "8747": GuildMember,
    "7486": GuildRankInformation,
    "7815": GuildRankMinimalInformation,
    "8454": GuildRankPublicInformation,
    "7809": HavenBagFurnitureInformation,
    "5089": ApplicationPlayerInformation,
    "6360": GuildApplicationInformation,
    "8232": GuildLogbookEntryBasicInformation,
    "7770": GuildLogbookChestActivity,
    "9063": GuildLevelUpActivity,
    "938": GuildPaddockActivity,
    "4533": GuildPlayerFlowActivity,
    "8587": GuildPlayerRankUpdateActivity,
    "5375": GuildRankActivity,
    "4586": GuildUnlockNewTabActivity,
    "7777": GuildRecruitmentInformation,
    "9536": AdditionalTaxCollectorInformations,
    "4461": TaxCollectorBasicInformations,
    "5471": TaxCollectorComplementaryInformations,
    "4585": TaxCollectorFightersInformation,
    "3257": TaxCollectorGuildInformations,
    "2224": TaxCollectorInformations,
    "6999": TaxCollectorLootInformations,
    "3004": TaxCollectorMovement,
    "4884": TaxCollectorWaitingForHelpInformations,
    "9946": HavenBagRoomPreviewInformation,
    "8261": AccountHouseInformations,
    "925": HouseGuildedInformations,
    "4132": HouseInformations,
    "6486": HouseInformationsForGuild,
    "6301": HouseInformationsForSell,
    "8889": HouseInformationsInside,
    "2394": HouseInstanceInformations,
    "630": HouseOnMapInformations,
    "1945": Idol,
    "984": PartyIdol,
    "821": InteractiveElement,
    "2919": InteractiveElementNamedSkill,
    "1108": InteractiveElementSkill,
    "4682": InteractiveElementWithAgeBonus,
    "1369": MapObstacle,
    "4603": StatedElement,
    "8846": SkillActionDescription,
    "4410": SkillActionDescriptionCollect,
    "6452": SkillActionDescriptionCraft,
    "6113": SkillActionDescriptionTimed,
    "9188": TeleportDestination,
    "4467": StorageTabInformation,
    "5765": UpdatedStorageTabInformation,
    "195": RecycledItem,
    "1958": EntityLook,
    "1647": IndexedEntityLook,
    "296": SubEntity,
    "9691": ItemDurability,
    "3474": MountClientData,
    "1109": UpdateMountBooleanCharacteristic,
    "1121": UpdateMountCharacteristic,
    "8274": UpdateMountIntegerCharacteristic,
    "2756": MountInformationsForPaddock,
    "6757": PaddockBuyableInformations,
    "7910": PaddockContentInformations,
    "5267": PaddockGuildedInformations,
    "6871": PaddockInformations,
    "2026": PaddockInformationsForSell,
    "2931": PaddockInstancesInformations,
    "4773": PaddockItem,
    "3404": CharacterCharacteristicForPreset,
    "7106": EntitiesPreset,
    "6623": ForgettableSpellsPreset,
    "3040": FullStatsPreset,
    "7555": IconNamedPreset,
    "6849": IdolsPreset,
    "3264": ItemForPreset,
    "3704": ItemsPreset,
    "4251": Preset,
    "3487": PresetsContainerPreset,
    "8632": SimpleCharacterCharacteristicForPreset,
    "5169": SpellForPreset,
    "5659": SpellsPreset,
    "5466": StatsPreset,
    "3363": AllianceInsiderPrismInformation,
    "5740": AlliancePrismInformation,
    "1437": PrismFightersInformation,
    "2839": PrismGeolocalizedInformation,
    "8665": PrismInformation,
    "2290": PrismSubareaEmptyInfo,
    "6559": Shortcut,
    "4540": ShortcutEmote,
    "1652": ShortcutEntitiesPreset,
    "5590": ShortcutObject,
    "893": ShortcutObjectIdolsPreset,
    "4430": ShortcutObjectItem,
    "968": ShortcutObjectPreset,
    "547": ShortcutSmiley,
    "7472": ShortcutSpell,
    "5062": AbstractSocialGroupInfos,
    "4544": AlliancedGuildFactSheetInformations,
    "1007": AllianceFactSheetInformations,
    "540": GuildFactSheetInformations,
    "9534": GuildInAllianceVersatileInformations,
    "5487": GuildInsiderFactSheetInformations,
    "597": GuildVersatileInformations,
    "3881": StartupActionAddObject,
    "1184": TrustCertificate,
    "1407": Version,
    "1340": BufferInformation
    }
    
    @classmethod
    def get_instance_id(cls,id,content):
        return cls.id_class[str(id)](content)
    